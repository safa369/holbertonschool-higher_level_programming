#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        new_mat = []
        new_mat = [[i * i for i in j]for j in matrix]
        return new_mat
