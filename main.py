import requests
import os
from urllib.parse import urlparse
import os.path
from datetime import datetime
from pprint import pprint
filename = 'hubble.jpeg'
dirname = 'images'
filepath = os.path.join(dirname, filename)
url = "https://dvmn.org/media/HST-SM4.jpeg"


def download_image(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs(dirname, exist_ok=True)

    with open(filepath, 'wb') as file:
        file.write(response.content)
def fetch_spacex_images():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    requests.exceptions.HTTPError
    links = (response.json()['links']['flickr']["original"])
    for  number, link in enumerate(links):
        file_path = f"images/{number}spacex.jpg"
        download_image(link, file_path)
def fetch_nasa_apod(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
    "api_key": api_key,
    "count": 30
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, picture in enumerate(response.json()):
        if picture['media_type'] != "image":
            continue
        image_url = picture['url']
        filepath = os.path.join("images", f"{number}nasa{get_extension(image_url)}")
        download_image(image_url, filepath)
def get_extension(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]
def fetch_nasa_epic(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
    "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, picture in enumerate(response.json()):
        pprint(picture['image'])
        date = datetime.fromisoformat(picture['date'])
        formated_date = date.strftime("%Y/%m/%d")
        print(formated_date)
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{picture['image']}.png"
        filepath = os.path.join("images", f"{number}nasa_epic.png")
        download_image(image_url, filepath, params=payload)
if __name__=="__main__":
    api_key = "W702mdYN3UlQOaM83AF2WRaS6YIHa8QVxNH5E1j1"
    fetch_spacex_images()
    fetch_nasa_apod(api_key)
    get_extension("https://example.com/txt/hello%20world.txt?v=9#python")
    fetch_nasa_epic(api_key)