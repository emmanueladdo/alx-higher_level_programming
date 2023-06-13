#!/usr/bin/python3
"""module with a function that adds attributes to objects."""


def add_attribute(obj, a, v):
    """Adds a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        a (str): The name of the attribute to add to obj.
        v (any): The value of attr.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
