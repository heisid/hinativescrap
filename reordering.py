#!/usr/bin/env python3
# Reordering column to username, natives, learning

import pandas as pd
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

df = pd.read_csv(inputfile)
df_reorder = df[['username','natives','learning']]
df_reorder.to_csv(outputfile, index=False)
