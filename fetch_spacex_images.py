import os

import requests
from dotenv import load_dotenv

from tools import download_image


def fetch_spacex_images(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']["original"]
    for  number, link in enumerate(links):
        file_path = os.path.join("images", f"{number}spacex.jpg")
        download_image(link, file_path)


if __name__=="__main__":
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    spacex_launch_id = os.getenv("SPACEX_LAUNCH_ID", "5eb87d47ffd86e000604b38a")
    fetch_spacex_images(spacex_launch_id)
