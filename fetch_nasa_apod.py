from tools import download_image, get_extension
import os
import requests
from dotenv import load_dotenv


def fetch_nasa_apod(api_key, photo_count):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
    "count": photo_count,
    "api_key": api_key,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, picture in enumerate(response.json()):
        if picture['media_type'] != "image":
            continue
        image_url = picture['url']
        filepath = os.path.join("images", f"{number}nasa{get_extension(image_url)}")
        download_image(image_url, filepath)

if __name__=="__main__":
    load_dotenv()
    os.makedirs("images", exist_ok=True)
    api_key = os.environ["NASA_API_KEY"]
    photo_count = os.getenv("PHOTO_COUNT", 20)
    fetch_nasa_apod(api_key, photo_count)
