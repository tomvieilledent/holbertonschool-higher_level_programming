#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = list(map(lambda row: list(
        map(lambda x: round(x / div, 2), row)), matrix))

    return (new_matrix)
