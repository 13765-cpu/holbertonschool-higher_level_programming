#!/usr/bin/python3
"""Script that sends a POST request and processes JSON response"""

import requests
import sys

if __name__ == "__main__":
    # Əgər argument yoxdursa boş string veririk
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    # POST request
    response = requests.post(url, data={'q': q})

    try:
        # JSON-a çevirməyə çalışırıq
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")

    except ValueError:
        # JSON parse olunmadısa
        print("Not a valid JSON")
