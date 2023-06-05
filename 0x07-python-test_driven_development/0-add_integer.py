#!/usr/bin/python3
""" Module add_integer
This is the  "Add Interger" module.
Returns the sum of a and b,
or raises an error if a and b are not integers or floats.
"""


def add_integer(a, b=98):
    """Returns the sum of a and b,
    or an error if a and b are not integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
