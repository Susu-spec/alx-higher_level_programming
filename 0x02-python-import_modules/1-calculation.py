#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div

    a = 10
    b = 5
    # operations - list of tuples
    operations = [('+', add), ('-', sub), ('*', mul), ('/', div)]
    for op, func in operations:
        result = func(a, b)
        print("{} {} {} = {}".format(a, op, b, result))
