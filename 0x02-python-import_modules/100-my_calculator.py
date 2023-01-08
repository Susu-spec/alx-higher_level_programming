#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, mul, div, sub


def main():
    args = len(argv[1:])
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Dict maps "operator chars to functions
    # Easier to read compared to if-else statements
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    # func is now the function associated with the operator
    func = operators[operator]

    result = func(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
