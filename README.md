# EgerakBot

## Overview
EgerakBot is a Telegram bot designed to facilitate employee attendance reporting. It allows employees to submit their location and status for the day, while automatically resetting their reports daily at midnight. The bot sends a summary of all reports to a designated chat, ensuring that all attendance information is collected and organized efficiently.

## Features
- Employee name selection through inline buttons.
- Daily report submission for location and status.
- Automatic summary reporting of employee statuses.
- Scheduled reset of reports at midnight.
- Multi-language support (Malay).

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Telegram Bot Token (create a new bot via [BotFather](https://t.me/botfather))

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Ardyshaz/egerakbot.git
   cd egerakbot
   
**Create and activate a virtual environment:**

python3 -m venv mybotenv
source mybotenv/bin/activate

**Install the required packages:**

pip install -r requirements.txt
Create a .env file in the project directory with your bot token and chat ID:

BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here

**Run the bot:**

python egerakbot.py

**Usage**
Start the bot by sending the /start command in your Telegram chat.
Select your name from the inline buttons.
Submit your location and status when prompted.
The bot will send a summary report of all submissions at the end of the day.

**Contributing**
Contributions are welcome! If you have suggestions for improvements or find bugs, feel free to open an issue or submit a pull request.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements**
python-telegram-bot for the Telegram bot framework.
APScheduler for scheduling tasks.
