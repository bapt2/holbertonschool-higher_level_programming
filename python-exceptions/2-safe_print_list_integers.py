#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                pos += 1
    except:
        raise (IndexError)
    print()
    return pos
