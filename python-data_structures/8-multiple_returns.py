#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        s = 0
        for i in sentence:
            s += len(i)
    tupple = (s, sentence[0][0])
    return tupple
