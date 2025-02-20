from lib.Telegram import TelegramAPI
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
ADMIN_UID = int(os.getenv("ADMIN_UID"))  # Convert to int

if not ADMIN_UID:
    raise ValueError("ADMIN_UID is missing!")

# Initialize Telegram API
telegram = TelegramAPI()

def Response(text, user_id, chat_id):
    try:
        # Check if the user is admin
        is_admin = user_id == ADMIN_UID

        if text == "hi" and is_admin:
            logging.info(f"Admin {user_id} said hi")
            telegram.send_message("Hi, you are Admin!", chat_id)
        elif text == "hi":
            logging.info(f"User {user_id} said hi")
            telegram.send_message("Hi!", chat_id)
        else:
            logging.info(f"No response for message: {text}")
    except Exception as e:
        logging.error(f"Error in Response function: {e}")