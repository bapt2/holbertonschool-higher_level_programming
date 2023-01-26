#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except:
        return None
    finally:
        if a or b != 0:
            print("Inside result: " + "{}".format(a / b))
        else:
            print("Inside result: {}" + str(None))
