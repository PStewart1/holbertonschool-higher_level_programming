#!/usr/bin/python3


def multiple_returns(sentence):
    n = len(sentence)
    char = None
    if len(sentence) > 0:
        char = sentence[0]
    tuple = (n, char)
    return tuple
