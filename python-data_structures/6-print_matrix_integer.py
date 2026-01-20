#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for pos in range(len(row)):
            if pos == len(row)-1:
                print("{:d}".format(row[pos]))
            else:
                print("{:d}".format(row[pos]), end=" ")
