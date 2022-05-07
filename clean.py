import pandas as pd

df = pd.read_csv("final.csv")

del df["Star_Name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Luminosity"]
del df["Unnamed: 6"]
del df["Unnamed: 0"]

df = df.dropna()

print(df)

df.to_csv("main.csv")