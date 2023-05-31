#!/usr/bin/python3
import math


class MagicClass:
    """
    A class representing a circle and providing methods to calculating its area
    and circumference.

    Attributes:
        radius (float or int): The radius of the circle.

    Methods:
        __init__(self, radius=0): Initializes a MagicClass object with the
        specified radius.
        area(self): Calculates and returns the area of the circle.
        circumference(self): Calculates and returns the circumference of the
        circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with the specified radius.

        Args:
            radius (float or int): The radius of the circle. Default is 0.

        Raises:
            TypeError: If the radius is not a number (float or int).
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        """
        Getter method for the radius property.

        Returns:
            float or int: The radius of the circle.
        """
        return self.__radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float or int: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float or int: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
