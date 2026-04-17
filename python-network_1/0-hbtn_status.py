#!/usr/bin/python3
"""Fetches a URL and displays response info"""
from urllib.request import urlopen
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
