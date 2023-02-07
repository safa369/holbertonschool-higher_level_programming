#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = len(matrix)
    b = len(matrix)
    new_mat = [[0] * b for i in range(a)]
    for i in range(a):
        for j in range(b):
            new_mat[i][j] = matrix[i][j] * matrix[i][j]
    return new_mat
