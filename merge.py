import pandas as pd
import sys

file = sys.argv[1]
file2 = sys.argv[2]

df1 = pd.read_csv(file)
df2 = pd.read_csv(file2)

df = pd.concat([df1, df2])
print(len(df))
df.to_csv("merged.csv", index=False)
