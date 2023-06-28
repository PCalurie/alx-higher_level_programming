#!/usr/bin/python3

def safe_print_integer_err(value):
    # handle possible errors
    try:
        # print the value as an int
        print("{:d}".format(value))
        # Return True if the print statement is true
        return True
    except Exception as e:
        # Import sys module to print the error to stderr
        import sys
        # Print the error message by the Exception: to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        # Return False if the print fails
        return False
