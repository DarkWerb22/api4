import telegram
from dotenv import load_dotenv
from time import sleep
import random
import os
if __name__=="__main__":
    load_dotenv()
    tg_token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    bot = telegram.Bot(token=tg_token)
    files_in_dir = os.listdir("images")
    sending_delay = os.getenv("SENDING_DELAY", "14400")
    while True:
        random_photo = random.choice(files_in_dir)
        photo_path = f"images/{random_photo}"
        with open(photo_path, 'rb') as photo:
            bot.send_photo(chat_id, photo=photo)
        sleep(int(sending_delay))