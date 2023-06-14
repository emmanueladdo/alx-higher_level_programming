#!/usr/bin/python3
"""file IO module which defines a textfile reading function."""


def read_file(filename=""):
    """Prints read content of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")
