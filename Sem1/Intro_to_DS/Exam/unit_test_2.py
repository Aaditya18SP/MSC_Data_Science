import pandas as pd
import seaborn as se
import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([[10,18],[26,34],[42,50]])
p1= pd.DataFrame(a1)
print(p1.iloc[1:, 0:1])
