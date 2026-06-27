#!/usr/bin/env python3
"""
Print a square with the character #

The size of the square must be the first argument 
of the program.
"""


import sys

if len(sys.argv) <= 1:
    sys.stderr.write("Missing argument\n")
    sys.stderr.write("Usage: ./1-print_square.py <size>\n")
    sys.stderr.write("Example: ./1-print_square.py 8\n")
    sys.exit(1)


size = int(sys.argv[1])

for i in range(size):
    for j in range(size):
        print("#", end="")
    print()
