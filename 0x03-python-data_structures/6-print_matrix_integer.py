#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for elem in lists:
            if elem == lists[len(lists) - 1]:
                print('{:d}'.format(elem))
                continue
            print(''.join('{:d}'.format(elem)), end=' ')
