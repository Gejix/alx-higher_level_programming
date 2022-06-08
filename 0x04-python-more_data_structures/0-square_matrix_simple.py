#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        new_matrix = []
        for i in matrix:
            newlist = list(map((lambda x: x * x), i))
            new_matrix.append(newlist)
        return (new_matrix)
