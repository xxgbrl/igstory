import time
import random
from instagrapi import Client
import requests
from instagrapi.exceptions import LoginRequired, ChallengeRequired
from utils.logger import log_message
from utils.telegram import telegram_monitor
from .auth import handle_login

USER_AGENTS = [
    "Instagram 289.0.0.77.109 Android (33/13; 420dpi; 1080x2400; samsung; SM-G998B; crownlte; qcom; en_US)",
    "Instagram 301.0.0.81.110 Android (34/14; 440dpi; 1080x2408; google; Pixel 7; panther; qcom; en_US)",
    "Instagram 295.0.0.32.110 Android (33/13; 480dpi; 1080x2400; OnePlus; ONEPLUS A6013; OnePlus6T; qcom; en_GB)",
]

def _perform_login_with_retries(cl: Client, config: dict) -> bool:
    """
    Attempts to log in up to 3 times with a delay between failures.
    """
    login_attempts = 0
    while login_attempts < 3:
        try:
            if handle_login(cl, config):
                return True
           
            login_attempts += 1
            if login_attempts < 3:
                log_message(f"Login failed. Retrying in 60 seconds... (Attempt {login_attempts} of 3)")
                time.sleep(60)
        except ChallengeRequired:
            log_message("Waiting 60 seconds for you to approve the login...")
            time.sleep(60)
           
            continue
    
    log_message("Login failed after 3 attempts. Stopping bot.")
    return False

def run_worker(config: dict, task_function):
    """
    Manages the main bot loop, including login, re-login, and interval waits.
    Executes a given task function in each cycle.
    """
    cl = Client()
    cl.private_requests = True

    cl.user_agent = random.choice(USER_AGENTS)
    log_message(f"Using User-Agent: ...{cl.user_agent[-50:]}")

    proxy = config.get('PROXY')
    if proxy:
        cl.set_proxy(proxy)
        log_message(f"Using proxy: {proxy}")

    cl.delay_range = [8, 16]

    if not _perform_login_with_retries(cl, config):
        return

    telegram_token = config.get('TELEGRAM_TOKEN')
    telegram_chat_id = config.get('TELEGRAM_CHAT')

    while True:
        try:
            cl.get_timeline_feed()
            task_function(cl, config)

            wait_end = time.time() + config['INTERVAL']
            telegram_monitor.next_run_time = time.strftime("%H:%M:%S", time.localtime(wait_end))
            while time.time() < wait_end:
                telegram_monitor.check_commands(telegram_token, telegram_chat_id)
                telegram_monitor.send_health_ping(telegram_token, telegram_chat_id)
                time.sleep(5)
        except LoginRequired as e:
            log_message(f"Session dead or expired: {e}. Attempting to re-login...")
            if not _perform_login_with_retries(cl, config):
                break
        except requests.exceptions.ConnectionError as e:
            log_message(f"Connection issue: {e}. Retrying in 5 minutes.")
            time.sleep(300)
        except Exception as e:
            log_message(f"Error in worker loop: {e}")
            time.sleep(60)
