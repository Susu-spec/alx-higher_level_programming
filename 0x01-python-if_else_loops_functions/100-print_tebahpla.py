#!/usr/bin/python3
# print alphabet in reverse wiith alternating cases at each iteration
for c in range(ord('z'), ord('a') - 1, -1):
    # ternary operator 'a if condition else b'
    i = 0 if c % 2 == 0 else 32
    print("{}".format(chr(c - i)), end='')
