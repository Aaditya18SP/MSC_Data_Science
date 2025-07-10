#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[19]:


data = pd.read_csv("../practical1/inpatientCharges.csv")
data.head()


# In[20]:


data.columns


# In[21]:


data.dtypes


# In[22]:


data[["procedure_code", "procedure_name"]]= data["DRG Definition"].str.split(" - ", expand=True)
data[["state_name", "region"]]= data["Hospital Referral Region Description"].str.split(" - ", expand=True)
data=data.drop(["Hospital Referral Region Description", "DRG Definition"],axis=1)


# In[23]:


print(data.dtypes)
data.head()


# In[24]:


data[" Average Covered Charges "] = data[" Average Covered Charges "].str.lstrip("$")
data[" Average Total Payments "] = data[" Average Total Payments "].str.lstrip("$")
data["Average Medicare Payments"] = data["Average Medicare Payments"].str.lstrip("$")

data= data.astype({"procedure_code":"int32","Average Medicare Payments":"float32", " Average Total Payments ": "float32", " Average Covered Charges ": "float32"})

data.head()


# In[37]:


data = data.select_dtypes("number")
print(data.columns)
data.head()


# In[26]:


data.corr()


# In[39]:


#heatmap
corr =data.corr()
plt.figure(figsize=(15,15))
plt.imshow(data.corr())

labels = data.columns
plt.xticks(ticks=np.arange(len(labels)), labels=labels)
plt.yticks(ticks=np.arange(len(labels)), labels=labels)
plt.tick_params(axis="x", labelrotation=90)

# Add correlation values to each cell
for i in range(len(labels)):
    for j in range(len(labels)):
        value = corr.iloc[i, j]
        plt.text(j, i, f'{value:.2f}', ha='center', va='center', color='black')
plt.show()


# In[49]:


plt.scatter(data[" Average Covered Charges " ], data[" Average Total Payments "],c=data["procedure_code"], cmap="plasma")
plt.xlabel(" Average Covered Charges ")
plt.ylabel(" Average Total Payments ")
plt.show()


# In[50]:


plt.scatter(data[" Average Covered Charges " ], data["Average Medicare Payments"], c=data["procedure_code"],cmap="coolwarm")
plt.xlabel(" Average Covered Charges ")
plt.ylabel("Average Medicare Payments")
plt.show()


# In[51]:


plt.scatter(data[" Average Total Payments " ], data["Average Medicare Payments"], c=data["procedure_code"],cmap="viridis")
plt.xlabel(" Average Total Payments ")
plt.ylabel("Average Medicare Payments")
plt.show()


# In[54]:


#Linear regression
x = data.loc[:, ["Average Medicare Payments"," Average Covered Charges "]]
y = data[" Average Total Payments "]



# In[59]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# In[60]:


x_tr, x_test, y_tr, y_test = train_test_split(x,y,test_size=0.2, random_state=200)


# In[61]:


model = LinearRegression().fit(x_tr, y_tr)


# In[62]:


print(model.coef_)
print(model.intercept_)


# In[63]:


test_pred = model.predict(x_test)
train_pred = model.predict(x_tr)


# In[64]:


print("Training R^2 score", r2_score(y_tr, train_pred))
print("Testing R^2 score",r2_score(y_test, test_pred) )


# # Inference
# Linear Regression fits the data very well and can help in accurate prediction. 
# This is indicated by the R^2 score which tells how much variation in the data is explained by the linear regression line which is 98% in testing data.
# In correlation analysis, we can see "Average Medicare Payments" is a very good predictor for "Average Total Payments". This is seen by the scatter plot which results in a very linear scatter plot.
