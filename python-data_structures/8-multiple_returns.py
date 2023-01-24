#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tr = (0, None)
    else:
        tr = (len(sentence), sentence[0])
    return tr
