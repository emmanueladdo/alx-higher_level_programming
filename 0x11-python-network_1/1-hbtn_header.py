#!/usr/bin/python3
# Take in a URL, sends request to URL and display value of `X-Request-Id
from sys import argv
from urllib.request as request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        print(res.info()['X-Request-Id'])
