#!/usr/bin/env python3

import pandas as pd
import sys

infile = sys.argv[1]

df = pd.read_csv(infile, index_col=0)
users = len(df.index)

learning = df.learning.str.split(",", expand=True).stack().value_counts().to_dict()
natives = df.natives.str.split(",", expand=True).stack().value_counts().to_dict()

print("Popularity Results")
print("==================\n")

print("\nNative Languages")
print("===================\n")
for key, value in [(k, natives[k]) for k in sorted(natives, key=natives.get, reverse=True)]:
    print("{:<32} {:>5} {:>6.3f}%".format(key, value, value*100/users))
print("\nLanguages of Interests")
print("==========================\n")
for key, value in [(k, learning[k]) for k in sorted(learning, key=learning.get, reverse=True)]:
    print("{:<32} {:>5} {:>6.3f}%".format(key, value, value*100/users))
