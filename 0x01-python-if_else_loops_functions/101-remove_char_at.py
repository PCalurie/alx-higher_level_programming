#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for c in range(len(str)):
        if c != n:
            copy += str[c]
    return copy
