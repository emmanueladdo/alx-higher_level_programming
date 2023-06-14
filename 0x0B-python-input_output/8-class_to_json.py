#!/usr/bin/python3
"""module that defines a class-to-JSON function."""


def class_to_json(obj):
    """Returns dictionary representation with a simple data structure."""
    return obj.__dict__
