#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the square.
Methods comparisons between Square objects and their sizes.
"""


class Square:
    """A class that defines a square by size and can compute area"""
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

    def __lestthan__(self, other):
        return self.__size < other.size

    def __lessequal__(self, other):
        return self.__size <= other.size

    def __equal__(self, other):
        return self.__size == other.size

    def __notequal__(self, other):
        return self.__size != other.size

    def __greaterthan__(self, other):
        return self.__size > other.size

    def __greaterequal__(self, other):
        return self.__size >= other.size
