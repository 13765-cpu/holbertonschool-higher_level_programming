#!/usr/bin/python3
"""Script that uses GitHub API to display user id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    # Basic Authentication ilə request
    response = requests.get(url, auth=(username, token))

    # JSON cavabı alırıq
    data = response.json()

    # id-ni çap edirik (əgər yoxdursa None çıxacaq)
    print(data.get("id"))
