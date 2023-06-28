#!/usr/bin/python3

def safe_function(fct, *args):
    # a try-except to handle possible errors
    try:
        # Call the func with the given args and return the result
        return fct(*args)
    except Exception as e:
        # import sys module
        import sys
        # print the error message by Exception: to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        # returns None if an error occurs
        return None
