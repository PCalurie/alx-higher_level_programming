#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # initialize new list to store result
    new_list = []
    # iterate over the range of list_length
    for i in range(list_length):
        # a handle possible errors
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            # handle case when second elmnt is 0
            print("division by 0")
            new_list.append(0)
        except TypeError:
            # handle case when an elmnt is not an integer or float
            print("wrong type")
            new_list.append(0)
        except IndexError:
            # handle when the list too short
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
