import pandas as pd
import sys

file = sys.argv[1]

df = pd.read_csv(file)

print(len(df))
df = df.drop_duplicates(subset=['title_tr'], keep='first')
df = df.drop_duplicates(subset=['body_tr'], keep='first')
df = df.drop_duplicates(subset=['body'], keep='first')
print(len(df))

df.to_csv(file, index=False)
