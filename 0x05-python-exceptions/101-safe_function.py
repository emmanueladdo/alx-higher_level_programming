#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        rt = fct(*args)
    except Exception as err:
        rt = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return rt
