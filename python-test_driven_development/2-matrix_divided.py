#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError
    ('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError
    ('matrix must be a matrix (list of lists) of integers/floats')
    l1 = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError
        ('matrix must be a matrix (list of lists) of integers/floats')
        if not (all(isinstance(element, (int, float)) for element in row)):
            raise TypeError
        ('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != l1:
            raise TypeError('Each row of the matrix must have the same size')
    matr_new = [[round(element / div, 2) for element in row] for row in matrix]
    return matr_new
