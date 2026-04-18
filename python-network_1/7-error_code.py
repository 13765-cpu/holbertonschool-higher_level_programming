#!/usr/bin/python3
"""Script that fetches a URL and handles HTTP errors"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # GET request göndəririk
    response = requests.get(url)

    # Status code yoxlanılır
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
