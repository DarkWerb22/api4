import telegram
from dotenv import load_dotenv
import os
if __name__=="__main__":
    load_dotenv()
    tg_token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    bot = telegram.Bot(token=tg_token)
    photo_path = "images/1nasa_epic.png"
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo=photo)