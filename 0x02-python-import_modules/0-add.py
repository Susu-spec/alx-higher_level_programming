#!/usr/bin/python3
#  run directly not when called via import
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
