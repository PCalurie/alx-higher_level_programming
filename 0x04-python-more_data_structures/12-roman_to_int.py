#!/usr/bin/python3
def roman_to_int(roman_string):
    # check if it is a string
    if not isinstance(roman_string, str):
        return 0
    # create a dictionary to store the values
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = []
    # loop through the roman values
    for i in range(len(roman_string)):
        current = values[roman_string[i]]
        # check for the standard Roman rules
        if i < len(roman_string) - 1 and values[roman_string[i + 1]] > current:
            result -= current
        else:
            result += current
        return result

