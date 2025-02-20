from lib.Telegram import TelegramAPI
from Responses import Response
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    offset = 0
    telegram = TelegramAPI()

    while True:
        try:
            data = telegram.get_updates(offset)
            if data and data.get("result"):
                for result in data["result"]:
                    try:
                        text = result["message"]["text"].lower()
                        chat_id = result["message"]["chat"]["id"]
                        user_id = result["message"]["from"]["id"]
                        logging.info(f"Received message: {text} from user {user_id} in chat {chat_id}")
                        Response(text, user_id, chat_id)
                    except KeyError:
                        logging.warning("Received non-text message or malformed data")
                    offset = result["update_id"] + 1
            else:
                logging.info("No new messages")
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
        time.sleep(1)  # Add a small delay to avoid spamming the API

if __name__ == "__main__":
    main()