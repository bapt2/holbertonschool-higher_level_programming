#!/usr/bin/python3
def uppercase(str):
    for o in str:
        if ord(o) >= 97 and ord(o) <= 122:
            c = ord(o)
            o = chr(c - 32)
        print("{}".format(o), end="")
    print("")
