#!/usr/bin/python3
from sys import argv


def main():
    args = len(argv[1:])
    if (args == 0):
        print("0 arguments.")
    else:
        print("{} argument{}:".format(args, 's' if args > 1 else ''))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
