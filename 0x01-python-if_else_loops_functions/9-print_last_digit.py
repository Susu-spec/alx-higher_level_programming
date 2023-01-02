#!/usr/bin/python3
def print_last_digit(number):
    if (not (isinstance(number, int))):
        return (0)
    number = abs(number)
    last_digit = number % 10
    print('{}'.format(last_digit), end='')
    return (last_digit)
