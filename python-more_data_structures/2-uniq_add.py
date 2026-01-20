#!/usr/bin/python3
def uniq_add(my_list=[]):
    added_num = []
    for i in range(len(my_list)):
        if my_list[i] not in added_num:
            added_num.append(my_list[i])
    result = sum(added_num)
    return(result)