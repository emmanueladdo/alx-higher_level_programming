#!/usr/bin/python3
"""The  Module matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    with the result of the division of matrix by div
    rounded to 2 decimal points.
    """

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for elemt in row:
            if not type(elemt) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    row_lengths = []
    for row in matrix:
        row_lengths.append(len(row))
    if not all(elem == row_lengths[0] for elem in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elemt / div, 2) for elemt in row] for row in matrix]

    return new_matrix
