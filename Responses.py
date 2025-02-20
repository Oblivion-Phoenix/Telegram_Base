from lib.Telegram import *

load_dotenv()
ADMIN_UID = int(os.getenv("ADMIN_UID"))  # Convert to int

if not ADMIN_UID:
    raise ValueError("ADMIN_UID is missing!")

def Response(text, user_id, chat_id):
    
    # Check if the user is admin
    is_admin = user_id == ADMIN_UID
    
    if text == "hi" and is_admin:
        print("Admin")
        say("hi you are Admin", chat_id)
    
    elif text == "hi":
        say("hi", chat_id)
        
    print("No Response")
