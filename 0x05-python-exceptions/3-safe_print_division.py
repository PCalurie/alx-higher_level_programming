#!/usr/bin/python3

def safe_print_division(a, b):
    # initialize a variable to store result
    result = None
    # handle possible errors
    try:
        result = a / b
    except ZeroDivisionError:
        # Handle the case when b is zero abd pass
        pass
    finally:
        # print the result
        print("Inside result: {}".format(result))
        # return the number of real integers
        return result
