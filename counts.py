#!/usr/bin/env python3

import pandas as pd
import sys

infile = sys.argv[1]

df = pd.read_csv(infile, index_col=0)

learning = df.learning.str.split(",", expand=True).stack().value_counts()
natives = df.natives.str.split(",", expand=True).stack().value_counts()

print("""
        Popularity Results
        ==================
        """)
print("\nNative Languages\n")
print(natives)
print("\nLanguages of Interests\n")
print(learning)
