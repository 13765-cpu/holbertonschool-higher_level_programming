#!/usr/bin/python3
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url, headers={"cfclearance": "true"})

    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
