#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_mat = []
    for i in matrix:
        mat = []
        for j in i:
            mat.append(j * j)
        new_mat.append(mat)
    return new_mat
