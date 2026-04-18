#!/usr/bin/python3
"""Script that sends a POST request with an email and displays the response body"""

import requests
import sys

if __name__ == "__main__":
    # Command line-dan URL və email götürürük
    url = sys.argv[1]
    email = sys.argv[2]

    # POST üçün data dictionary şəklində g
    data = {'email': email}

    # POST request göndəririk
    response = requests.post(url, data=data)

    # Response body-ni çap edirik
    print(response.text)
