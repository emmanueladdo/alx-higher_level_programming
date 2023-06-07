#!/usr/bin/python3
"""Module finds the maximum integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None

    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num

    return max_value
