#!/usr/bin/python3

def magic_calculation(a, b):
    # a variable to store the result
    result = 0
    # iterate over the range from 1 to 3
    for i in range(1, 3):
        # Use a try-except to handle possible errors
        try:
            # raise an exception with a message if iis greater than a
            if i > a:
                raise Exception("Too far")
            # Otherwise, equate the result with a power and division operatiion
            else:
                result += (a ** b) / i
        # If an exception occurs, equate the result with addition
        except Exception:
            result = b + a
            break
    # Return the result of the operation
    return result
