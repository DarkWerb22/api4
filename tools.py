import os
import os.path
from urllib.parse import urlparse

import requests


def download_image(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    parsed_url = urlparse(url)
    _, extension = os.path.splitext(parsed_url.path)
    return extension