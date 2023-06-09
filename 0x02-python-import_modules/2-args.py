#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1
args = sys.argv[1:]

print("Number of argument(s):", argc)
print("Argument(s):", end=" ")
print(", ".join(args) + ("." if argc == 0 else ":"))

if argc > 0:
    for i, arg in enumerate(args, start=1):
        print(i, ":", arg)
