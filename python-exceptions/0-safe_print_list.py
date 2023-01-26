#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pos = 0
    try:
        for i in range(x):
            pos += 1
            print("{}".format(pos), end="")
        print()
        return pos
    except:
        print()
        return pos
