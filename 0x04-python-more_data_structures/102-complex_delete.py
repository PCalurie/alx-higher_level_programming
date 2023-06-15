#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # create a list of the keys to be deleted
    keys_to_delete = []
    # loop through each key/value in the dictionary
    for key, val in a_dictionary.items():
        # check if the value matches the ome searched
        if val == value:
            # append the key to the list of keys to delete
            keys_to_delete.append(key)
    # loop through each key in the list of keys to delete
    for key in keys_to_delete:
        # use dictionary pop method to remove key
        a_dictionary.pop(key)
    return a_dictionary
