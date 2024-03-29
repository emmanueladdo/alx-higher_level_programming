#!/usr/bin/python3
"""this fetches https://intranet.hbtn.io/status"""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        if response.readable():
            data = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(data)))
            print("\t- content: {}".format(data))
            print("\t- utf8 content: {}".format(data.decode("utf-8")))
