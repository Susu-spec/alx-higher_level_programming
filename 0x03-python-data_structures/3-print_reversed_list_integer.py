#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    # if list is empty, return none
    if not my_list:
        return None
    for i in range(idx, -1, -1):
        if type(my_list[i]) == int:
            print("{}".format(my_list[i]))
