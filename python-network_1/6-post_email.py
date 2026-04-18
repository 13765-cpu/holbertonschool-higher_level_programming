#!/usr/bin/python3
"""Script that sends a POST request with an email and displays the response body"""
import requests
import sys
if __name__ == "__main__":
    # Command line-dan URL və email götür�
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
