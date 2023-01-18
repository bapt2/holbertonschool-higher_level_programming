#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = sum(int(i) for i in sys.argv[1:])
    print(res)
