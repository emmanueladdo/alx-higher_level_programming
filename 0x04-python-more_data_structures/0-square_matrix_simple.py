#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix.append([list(map(lambda n: n**2, subl)) for subl in matrix])
    return new_matrix
