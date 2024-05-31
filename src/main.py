import logging
import os
import importlib
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from telethon import TelegramClient, events

from Commands import startCommand

# load the .env file
load_dotenv()

# Create the client and connect
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
bot = TelegramClient('bot', int(api_id), api_hash).start(bot_token=bot_token)


try:
    # Logging configuration
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # RotatingFileHandler
    max_log_size_mb = 5  # Set your desired maximum log size in megabytes
    file_handler = RotatingFileHandler('./bot.log', maxBytes=max_log_size_mb * 1024 * 1024, backupCount=1)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)

    # commands_dir = os.path.join(os.path.dirname(__file__), 'Commands')
    # commands = {}
    #
    # for folderName in os.listdir(commands_dir):
    #     if folderName.endswith('.py') and folderName != '__init__.py':
    #         command_name = os.path.splitext(folderName)[0]
    #         command = importlib.import_module(f'Commands.{command_name}')
    #         commands[command_name] = command
    #
    # logging.info("Main script runs successfully, Bot is working")

    # Start command
    @bot.on(event=events.NewMessage(pattern='/start'))
    async def handle_start_command(event):
        await startCommand.send_welcome(event, bot)
        # if 'startCommand' in commands:
        # commands['startCommand'].send_welcome(event, bot)

    bot.run_until_disconnected()
except KeyboardInterrupt:
    logging.info("Polling manually interrupted.")
