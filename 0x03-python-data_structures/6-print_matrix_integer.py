#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rol in range(len(matrix)):
        for col in range(len(matrix[rol])):
            if col != 0:
                print(" ", end="")
            print("{:d}".format(matrix[rol][col]), end='')
        print()
