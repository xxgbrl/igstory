# Instagram Story Auto-Viewer Bot

```
   _         _____  ___         _____  __  __    __   __   _____  ___  __      
  /_\  /\ /\/__   \/___\ /\   /\\_   \/__\/ / /\ \ \ / _\/__   \/___\/__\/\_/\
 //_\\/ / \ \ / /\//  // \ \ / / / /\/_\  \ \/  \/ / \ \   / /\//  // \//\_ _/
/  _  \ \_/ // / / \_//   \ V /\/ /_//__   \  /\  /  _\ \ / / / \_// _  \ / \ 
\_/ \_/\___/ \/  \___/     \_/\____/\__/    \/  \/   \__/ \/  \___/\/ \_/ \_/ V.1
                                                                   
```
If you find this tool useful, don't forget to **star ⭐** this repository and **follow my GitHub account** for future projects\!

## Main Features

- **Interactive Setup**: Configuring the bot for the first time is made easy with a guide directly in the terminal.
- **Session Management**: Saves the login session to avoid repeated logins that could trigger Instagram's suspicion.
- **Anti-Double View**: The bot records stories that have been viewed and will not view them again within 24 hours, saving resources and mimicking normal behavior.
- **Random Delay**: Uses variable time intervals between actions to avoid detection as bot activity.
- **Random Sampling Following**: If you follow many accounts, the bot will select a random sample according to the specified limit (`MAX_FOLLOWING`) for each session, reducing the risk of being blocked.
- **Telegram Integration**:
  - Status reports when the bot starts and after each cycle is completed.
  - `/status` command to check the bot's status, uptime, and latest logs at any time.
  - Periodic "Health Ping" notifications to ensure the bot is still running.
- **Proxy Support**: Can route traffic through an HTTP proxy for added security.
- **Complete Logging**: All activities are logged to the console and the `bot.log` file for easy debugging.
- **Universal Compatibility**: Equipped with a patch to ensure compatibility with various versions of `instagrapi`.

## Prerequisites

- Python 3.8 or newer.

## Installation

1.  **Clone or Download the Project**
    ```bash
    git clone https://github.com/cenmurong/igstory
    cd igstory
    ```
    Or download the ZIP file and extract it.

2.  **Install Dependencies**
    Open a terminal or command prompt in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Bot for the First Time**
    Open a terminal in the project folder and run the command:
    ```bash
    python3 igstory.py
    ```

2.  **Follow the Interactive Setup**
    When run for the first time, the bot will ask you to enter:
    - Instagram Username & Password.
    - Telegram Token & Chat ID (optional).
    - Configuration for interval, following limit, and proxy.

    Once completed, the configuration will be saved in the `.env` file.

3.  **Running the Bot Subsequently**
    Just run the same command again. The bot will read the configuration from `.env` and the session from `ig_session.json` to log in automatically.
    ```bash
    python3 igstory.py
    ```

## Configuration

All configurations are stored in the automatically created `.env` file.

- `INSTAGRAM_USERNAME`: Your Instagram account username.
- `INSTAGRAM_PASSWORD`: Your Instagram account password.
- `TELEGRAM_BOT_TOKEN`: API token from your Telegram bot (obtainable from @BotFather).
- `TELEGRAM_CHAT_ID`: Unique ID of your chat with the bot (obtainable from @userinfobot).
- `CHECK_INTERVAL`: Time interval (in seconds) between each story viewing cycle. Default: `600`.
- `MAX_FOLLOWING`: The maximum number of following accounts whose stories will be checked in one cycle. Default: `100`.
- `PROXY`: HTTP proxy address (example: `http://user:pass@ip:port`). Leave empty if not used.

## File Structure

After running, the bot will create several files:

- `.env`: Stores your credentials and configuration. **Do not share this file.**
- `ig_session.json`: Stores Instagram login session data.
- `seen_stories.json`: Database of stories that have been viewed to prevent double-viewing.
- `bot.log`: Log of all bot activities.

## Connect With Me

<p>
  <a href="https://x.com/cenmurong"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" /></a>
  <a href="https://discord.com/users/451101979331002370"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" /></a>
  <a href="https://instagram.com/asaptrfr"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
</p>

## Disclaimer

The use of bots to automate activities on social media platforms like Instagram carries risks, including temporary or permanent restrictions on your account. Use this bot wisely and at your own risk. The developer is not responsible for any consequences that may arise from the use of this script.
