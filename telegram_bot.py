import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID= os.getenv("TELEGRAM_CHAT_ID")

async def send_message(message: str):
    """
    Sends a message to a specified chat using a Telegram bot.
    Args:
        message (str): The message to be sent.
    Returns:
        None
    """
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)
    
if __name__ == "__main__":
    asyncio.run(send_message("Esto es una prueba"))