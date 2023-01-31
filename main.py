import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
import os.path
filename = 'hubble.jpeg'
dirname = 'images'
filepath = os.path.join(dirname, filename)
url = "https://dvmn.org/media/HST-SM4.jpeg"


def download_image(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)

def get_extension(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]
1
if __name__=="__main__":
    os.makedirs(dirname, exist_ok=True)
    load_dotenv()
    api_key = os.getenv("API_KEY")
    fetch_nasa_apod(api_key)
    get_extension("https://example.com/txt/hello%20world.txt?v=9#python")
    fetch_nasa_epic(api_key)