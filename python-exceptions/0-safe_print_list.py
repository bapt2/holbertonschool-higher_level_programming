#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pos = 0
    try:
        for i in range(x):
            print("{}".format(my_list[pos]), end="")
            pos += 1
        print()
        return pos
    except:
        print()
        return pos
