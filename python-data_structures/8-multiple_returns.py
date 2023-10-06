#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, "None")
    a = len(sentence)
    f_char = sentence[0]
    return (a, f_char)
