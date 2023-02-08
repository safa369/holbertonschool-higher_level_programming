#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        a = len(matrix)
        
        new_mat = [[0] * a for i in range(a)]
        for i in range(a):
            for j in range(0, a - 1):
                new_mat[i][j] = matrix[i][j] ** 2
        return new_mat
