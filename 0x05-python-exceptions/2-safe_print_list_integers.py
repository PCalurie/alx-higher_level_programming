#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
# iterate through the values of x
    for i in range(x):
        try:
            print("{:d}".format(my_list[i], end=""))
# catch errors
        except (ValueError, TypeError):
            pass
        else:
            count += 1
# print the number of real integers
    print()
    return count
