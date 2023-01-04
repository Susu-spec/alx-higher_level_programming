#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    copy = []
    for i in range(length):
        if i != n:
            copy.append(str[i])
    copy = "".join(copy)  # Convert list to string
    return (copy)
