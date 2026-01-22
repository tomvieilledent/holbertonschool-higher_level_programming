#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (array of arrays of integers/floats)")
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    

    new_matrix = list(map(lambda row: list(
        map(lambda x: round(x / div, 2), row)), matrix))

    return (new_matrix)
