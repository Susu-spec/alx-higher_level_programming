#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # if list is empty, return none
    if not my_list:
        return None
    idx = len(my_list) - 1
    # similar to reverse()
    for i in range(idx, -1, -1):
        print("{:d}".format(my_list[i]))
