#!/usr/bin/python3
for c in range(10):
    for o in range(10):
        if c < o:
            if c == 8 and o == 9:
                print("{:d}{:d}".format(c, o))
            else:
                print("{:d}{:d}".format(c, o), end=", ")
