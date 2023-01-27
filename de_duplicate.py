import pandas as pd


df = pd.read_csv("all_translated.csv")

print(len(df))
df = df.drop_duplicates(subset=['title_tr'], keep='first')
df = df.drop_duplicates(subset=['body_tr'], keep='first')
df = df.drop_duplicates(subset=['body'], keep='first')
print(len(df))

df.to_csv("all_translated.csv", index=False)