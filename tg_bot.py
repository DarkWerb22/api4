import telegram
from dotenv import load_dotenv
import os
if __name__=="__main__":
    load_dotenv()
    tg_token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    bot = telegram.Bot(token=tg_token)
    print(bot.get_me())
    bot.send_message(chat_id, "Hello World")