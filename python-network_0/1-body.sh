#!/bin/bash
# Display body only if HTTP status code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && curl -s "$1"
