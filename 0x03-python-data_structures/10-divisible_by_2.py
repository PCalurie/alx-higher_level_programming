#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # create an empty list to store the result from the list
    result = []

    for i in my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
