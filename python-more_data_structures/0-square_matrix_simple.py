#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return new_matrix

# map extérieur  → lignes                    list(map(lambda row)) donne une matrice
# map intérieur  → éléments                  list(map(lambda x)) donne une ligne
# lambda row     → transforme une ligne
# lambda x       → transforme un élément
# list()         → matérialise le résultat