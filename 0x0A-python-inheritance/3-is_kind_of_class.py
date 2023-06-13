#!/usr/bin/python3
"""Defines a check function for intances of classes and super classes."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class True.
        Otherwise False.
    """
    return isinstance(obj, a_class)
