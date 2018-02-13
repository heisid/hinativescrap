#!/usr/bin/env python3
"""
This script is used to clean results file (csv formatted),
removing non-existent users (maybe Unregistered user) from the rows
Usage: python cleaning.py inputfile outputfile
"""

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        if line == ",\n":
            pass
        else:
            fout.write(line)


