import os
import requests
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

class TelegramAPI:
    def __init__(self):
        self.API_KEY = os.getenv("TELEGRAM_API_KEY")
        if not self.API_KEY:
            raise ValueError("Telegram API Key is missing!")
        self.base_url = f"https://api.telegram.org/bot{self.API_KEY}"

    def get_updates(self, offset=0, limit=100):
        """
        Fetch new messages using the Telegram API.
        """
        try:
            parameters = {"offset": offset, "limit": limit}
            response = requests.get(f"{self.base_url}/getUpdates", params=parameters)
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"API Error: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            logging.error(f"Error in get_updates: {e}")
            return None

    def send_message(self, text, chat_id, reply_markup=None):
        """
        Send a message using the Telegram API.
        """
        try:
            parameters = {"chat_id": chat_id, "text": text}
            if reply_markup:
                parameters["reply_markup"] = reply_markup
            response = requests.post(f"{self.base_url}/sendMessage", json=parameters)
            if response.status_code != 200:
                logging.error(f"API Error: {response.status_code} - {response.text}")
            return response.status_code == 200
        except Exception as e:
            logging.error(f"Error in send_message: {e}")
            return False

    def send_keyboard(self, text, chat_id, keyboard):
        """
        Send a message with an inline keyboard.
        """
        markup = {"keyboard": keyboard, "resize_keyboard": True}
        return self.send_message(text, chat_id, reply_markup=markup)