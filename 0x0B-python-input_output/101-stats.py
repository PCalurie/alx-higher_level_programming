#!/usr/bin/python3
"""Script that reads stdin line by line and computes the metrics"""


import sys


# Initialize the total file size and the status codes dictionary
total_size = 0
status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }


# Define the function to print the statistics
def print_stats():
    """Prints the statistics in file"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


# Use a try-except block to handle keyboard interruption errs
try:
    # Loop through the lines from stdin
    for i, line in enumerate(sys.stdin, 1):
        # Split the line using spaces
        tokens = line.split()
        # update the total size and the status code counts
        if len(tokens) > 2:
            size = tokens[-1]
            code = tokens[-2]
            if size.isdigit():
                total_size += int(size)
            if code in status_codes:
                status_codes[code] += 1
        # If the line number is a multiple of 10, print the statistics
        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    # Print the statistics before you exit
    print_stats()
    raise
