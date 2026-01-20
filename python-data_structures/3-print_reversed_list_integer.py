#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenth = len(my_list)
    for i in my_list:
        print("{:i}".format(my_list[lenth - i]))
