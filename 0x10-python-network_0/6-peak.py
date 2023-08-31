#!/usr/bin/python3
"""Algorithms for peak in list of integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int: The peak element in the list.
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
