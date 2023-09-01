#!/usr/bin/python3
# Take in a URL, sends request to URL and display value of `X-Request-Id
from sys import argv
from urllib.request as request

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
