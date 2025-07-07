#univariate analysis
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Practicals/Practical_5_Univariate_Analysis/Boston.csv")

data = data.drop(columns=["Unnamed: 0"])
print(data.head())
total_rows = data.shape[0]
# percent of outliers in each column
summary = data.describe()
print(summary)

for col in summary.columns:
    min_val = summary.loc["min",col]
    max_val = summary.loc["max", col]
    q3 = summary.loc["75%",col]
    q1 = summary.loc["25%", col]
    iqr = q3-q1
    upper_limit = min(max_val,q3+(1.5*iqr))
    lower_limit = max(min_val,q1-(1.5*iqr))

    outlier_rows = data[(data[col] > upper_limit) | (data[col]<lower_limit)].shape[0]
    outlier_percent = outlier_rows/total_rows

    print(col + " : "+str(outlier_percent))

#display the box plot for each column
fig, axes = plt.subplots(ncols=4, nrows=4,figsize=(10,15))
axes= axes.flatten()
index =0

for k,v in data.items():
    axes[index].set_ylabel(k)
    axes[index].boxplot(v)
    index+=1
plt.tight_layout(pad=0.4, w_pad=0.4, h_pad=0.4)
plt.show()


#skewness and kurtosis
fig, axes = plt.subplots(ncols=4, nrows=4,figsize=(10,15))
axes= axes.flatten()
index =0
for k, v in data.items():
    axes[index].set_xlabel(k)
    axes[index].hist(v, density=True)
    print(k +": skewness "+ str(v.skew())+ ": kurtosis " + str(v.kurtosis()))
    index +=1
plt.show()

#show correlation
corr = data.corr()

fig,ax= plt.subplots()
ax.imshow(corr)

ax.set_xticks(range(len(data.columns)), labels = data.columns)
ax.set_yticks(range(len(data.columns)), labels = data.columns)

for i in range(len(data.columns)):
    for j in range(len(data.columns)):
        ax.text(j, i, "{:.2f}".format(corr.iloc[i,j]), ha="center", va="center", color="w")

plt.show()

#scatter plot
fig, ax = plt.subplots(ncols= len(data.columns), nrows= len(data.columns) , figsize=(10,10))
ax =ax.flatten()
index =0

columns = data.columns
i=0
j=0
while i < len(columns):
    j=0
    while j < len(columns):
        if i<=j:
            j+=1
            continue
        col1= columns[i]
        col2=columns[j]
        print(col1, col2)
        ax[index].scatter(data[col1], data[col2])
        j+=1
        index+=1
    i+=1
plt.show()
