#!/usr/bin/python3
def add(a, b):
    return a + b


def main():
    a = 1
    b = 2
    print('{} + {} = {}'.format(a, b, add(a, b)))


#  run directly not when called via import
if __name__ == "__main__":
    main()
