#!/usr/bin/python3

# check if character is lowercase
def islower(c):
    if (ord(c) == 97 or (ord(c) > 97 and ord(c) < 123)):
        return True
    else:
        return False
