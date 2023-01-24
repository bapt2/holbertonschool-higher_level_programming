#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == "":
        tr = (0, None)
    tr = (len(sentence), sentence[0])
    return tr
