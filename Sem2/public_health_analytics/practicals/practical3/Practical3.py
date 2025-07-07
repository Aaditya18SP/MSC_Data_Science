#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[10]:


data = pd.read_csv("practical3/breast_cancer.csv")
data.head()


# In[6]:


print(data.columns)


# In[8]:


print(data.shape)
print(data["diagnosis"].unique())


# In[17]:


data.loc[data["diagnosis"]=="M", "diagnosis"] = 1
data.loc[data["diagnosis"]=="B", "diagnosis"] =0
data = data.astype({"diagnosis": "int64"})
print(data.dtypes)
data.head()


# In[24]:


corr = data.corr()
corr = corr.loc["diagnosis"]
corr[corr>0.65]


# In[26]:


x = data[["radius_mean", "perimeter_mean", "area_mean", "concavity_mean", "concave points_mean", "radius_worst", "perimeter_worst", "area_worst","concavity_worst", "concave points_worst"]]
x.head()


# In[29]:


y = data["diagnosis"]


# In[30]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[31]:


x_tr, x_test, y_tr, y_test = train_test_split(x,y,test_size=0.2, random_state=200)


# In[33]:


model = LogisticRegression(max_iter=500).fit(x_tr, y_tr)


# In[34]:


tr_pred = model.predict(x_tr)
test_pred = model.predict(x_test)


# In[42]:


print(classification_report(y_tr,tr_pred))


# In[41]:


print(classification_report(y_test,test_pred))


# In[39]:


confusion_matrix(y_tr,tr_pred)


# In[40]:


confusion_matrix(y_test,test_pred)


# # Inference
# - The model successfully predicts and gives good results for class 0 which stands for Benign Diagnosis. A 90% precision and 93% recall rate is a good indicator
# - The model's precision and recall score for class 1 standing for Malignant diagnosis reduces compared to class 0. With 86% precision and 79% recall rate, the model accuracy takes a hit.
# - Overall, the model fits the data quite well using the chosen features
# - The features were chosen who had a correlation of 0.65 or greater.

# In[ ]:




