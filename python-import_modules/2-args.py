#!/usr/bin/python3
if __name__ == "__main__":
        import sys
        for i in range(0, len(sys.argv)):
                i += 1
                i = i - 1
        if i == 1:
                print("{} argument:".format(i))
        elif i == 0:
                print("{} argument:".format(i))
        else:
                print("{} argument:".format(i))
        for x in range(0, len(sys.argv)):
                if x != 0:
                        print("{}: {}".format(x, sys.argv[x]))
