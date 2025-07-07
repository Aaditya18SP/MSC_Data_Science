import pandas as pd

data = pd.read_csv("../Practicals/Practical_7_Data_Wrangling/youtube.csv")
print(data.head())


print(data.groupby("Rank").sum())
#print(data.groupby("Rank").agg({"Col":"max", "Col2": lambda x: x**2}))


print(data.sort_values("Rank", key=lambda x: x.str.lower(), ascending=False))

