import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TELEGRAM_API_KEY")

if not API_KEY:
    raise ValueError("Telegram API Key is missing!")

base_url = f"https://api.telegram.org/bot{API_KEY}"

def read_message(offset):
    parameters = {"offset": offset, "limit": 1}
    response = requests.post(f"{base_url}/getUpdates", json=parameters)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def say(text, chat_id):
    parameters = {"chat_id": chat_id, "text": text}
    response = requests.post(f"{base_url}/sendMessage", json=parameters)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")