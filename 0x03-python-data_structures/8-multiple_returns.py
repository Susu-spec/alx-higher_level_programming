#!/usr/bin/python3
# tuples return muliple values from a function
def multiple_returns(sentence):
    if not sentence:
        first = None
    else:
        first = sentence[0]
    length = len(sentence)
    return length, first
