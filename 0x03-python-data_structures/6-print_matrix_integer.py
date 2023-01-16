#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for elem in lists:
            if elem == lists[len(lists) - 1]:
                print('{}'.format(elem))
                continue
            print(''.join('{}'.format(elem)), end=' ')
