from main import download_image, get_extension
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
def fetch_nasa_epic(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
    "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, picture in enumerate(response.json()):
        date = datetime.fromisoformat(picture['date'])
        formated_date = date.strftime("%Y/%m/%d")
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{picture['image']}.png"
        filepath = os.path.join("images", f"{number}nasa_epic.png")
        download_image(image_url, filepath, params=payload)

if __name__=="__main__":
    load_dotenv()
    os.makedirs("images", exist_ok=True)
    api_key = os.getenv("API_KEY")
    fetch_nasa_epic(api_key)