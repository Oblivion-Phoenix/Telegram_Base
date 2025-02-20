from lib.Telegram import *
from Responses import *


offset = 0

while True:
    data = read_message(offset)
    if data["result"]:
        for result in data["result"]:
            try:
                text = result["message"]["text"].lower()
                chat_id = result["message"]["chat"]["id"]
                user_id = result["message"]["from"]["id"]
                print(result)
                Response(text, user_id, chat_id)
            except:
                print("not a text")
            offset = data["result"][-1]["update_id"] + 1
    else:
        print(data)
