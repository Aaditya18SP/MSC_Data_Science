import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("../Practicals/Practical_6_Correlation_analysis/CarPrice_Assignment.csv")

print(data.dtypes)

data = data.select_dtypes(include=["int64","float64"])
print(data.head())

corr= data.corr()
print(corr.head())

fig,axes = plt.subplots()
axes.imshow(corr)
axes.set_xticks(range(len(data.columns)), labels=data.columns, rotation=45)
axes.set_yticks(range(len(data.columns)), labels= data.columns)

for i in range(len(data.columns)):
    for j in range(len(data.columns)):
        axes.text(j, i , "{:.2f}".format(data.iloc[i,j]), ha="center", va="center",color="w")
fig.tight_layout()
import matplotlib.pyplot as plt
plt.show()


