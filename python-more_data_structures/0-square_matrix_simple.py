#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        a = len(matrix)
        
        new_mat = [[matrix[i][j] ** 2 for i in range(a)] for j in range(a)]
        return new_mat
