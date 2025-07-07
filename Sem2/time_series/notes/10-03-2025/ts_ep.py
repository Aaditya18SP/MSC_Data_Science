import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("electric_production.csv")
print(data.head())

columns = data.columns
data = data.astype({columns[0]: "datetime64[ns]", columns[1]:"float32"})

plt.plot(data.loc[:50,columns[0]], data.loc[:50, columns[1]])
plt.xlabel("date")
plt.tick_params(labelrotation=90)
plt.ylabel("production numbers")
plt.show()
