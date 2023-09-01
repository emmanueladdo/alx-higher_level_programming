#!/usr/bin/python3
# Take in a URL, sends request to URL and display value of `X-Request-Id
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
