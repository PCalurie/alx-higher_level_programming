#!/usr/bin/python3
"""Script that adds all arguments to a Python list, then saves them to a file
in a specified serialization formtat"""


import sys
from os import path


# Import functions from the previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# The name of the file to be saved to
filename = "add_item.json"

# If the file exists, load the list from it, otherwise create an empty list
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all the arguments passed to the list
my_list.extend(sys.argv[1:])

# Save the list as a JSON representation in the file
save_to_json_file(my_list, filename)
