#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix
    """
    new_matrix = []
    for col in matrix:
        res = list(map(lambda x: x**2, col))
        new_matrix.append(res)
    return new_matrix        