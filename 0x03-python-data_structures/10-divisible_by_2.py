#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if not my_list:
        return None
    for elem in my_list:
        new_list += [True if elem % 2 == 0 else False]
    return new_list
