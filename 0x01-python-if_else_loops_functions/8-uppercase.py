#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
