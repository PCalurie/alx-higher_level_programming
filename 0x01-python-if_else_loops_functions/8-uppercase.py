#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            i = chr(ord(i))
        print("{}".format(i), end="")
    print()
