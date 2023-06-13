#!/usr/bin/python3

def no_c(my_string):
    # initialize and empty string to store the result
    new_string = ""
    # loop through the string
    for n in my_string:
        if n not in "cC":
            new_string += n
    return new_string
