#!/usr/bin/python3
"""
This is a "Square"  module.

Module provides a simple Square class with initialize size.
Default size is 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for the size.
Method area returns area of the square.
Method my_print prints the square using "#".
"""


class Square:
    """A class that defines a square by size, which defaults 0.
    Square also gets area, and print square using '#'.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is 0:
            print()
        for length in range(self.__size):
            print("#" * self.__size)
