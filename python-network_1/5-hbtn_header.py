#!/usr/bin/python3
# Script sends a request to a URL and displays X-Request-Id from response header
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
