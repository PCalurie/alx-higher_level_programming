#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_set = set()

    for x in my_list:

        unique_set.add(x)

    total = 0

    for x in unique_set:
        total += x
    return total
