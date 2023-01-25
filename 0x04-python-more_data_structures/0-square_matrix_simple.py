#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix_o = []
    for row in matrix:
        square_matrix_i = []
        for i in range(len(row)):
            square_matrix_i.append(row[i] * row[i])
        square_matrix_o.append(square_matrix_i)
    return (square_matrix_o)
