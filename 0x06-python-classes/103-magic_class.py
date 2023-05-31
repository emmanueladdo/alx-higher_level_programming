#!/usr/bin/python3
import math
"""
This is the "MagicClass" module.
This provides a simple Magic Class cals circumference 
"""

class MagicClass:
    """
    A class representing a magic circle.

    Attributes:
        __radius (float): The radius of the magic circle.
    """

    def __init__(self, radius):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
