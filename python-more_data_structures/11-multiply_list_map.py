#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        new_list[i] *= number
    return new_list
