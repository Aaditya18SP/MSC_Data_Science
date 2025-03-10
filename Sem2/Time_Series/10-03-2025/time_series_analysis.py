import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("min_temp_dataset.csv")

print(data.head())

columns = data.columns

data = data.astype({columns[0]: "datetime64[ns]",columns[1]:"float32"})


plt.plot(data.loc[30:100,columns[0]], data.loc[30:100,columns[1]])
plt.xlabel("date")
plt.tick_params(labelrotation=90)
plt.ylabel("max_temp")
plt.show()
