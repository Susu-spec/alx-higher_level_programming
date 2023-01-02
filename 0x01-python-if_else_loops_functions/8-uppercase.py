#!/usr/bin/python3

# check if a character is a letter
def is_letter(ch):
    ch_code = ord(ch)
    if (65 <= ch_code <= 90) or (97 <= ch_code <= 122):
        return True
    else:
        return False


# check if uppercase
def is_upper(ch):
    if (65 <= ord(ch) <= 90):
        return True
    else:
        return False


# convert to uppercase
def uppercase(str):
    result = ''
    for letter in str:
        if (is_letter(letter) is False) or (is_upper(letter) is True):
            result += letter
            continue
        ch_code = ord(letter) - 32
        char = chr(ch_code)
        result += char
    print('{}'.format(result))
