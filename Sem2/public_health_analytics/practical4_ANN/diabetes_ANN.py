#!/usr/bin/env python
# coding: utf-8

# In[29]:


import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt


# In[30]:


data = pd.read_csv("diabetes.csv")
data.head()


# In[3]:


data.shape


# In[50]:


#class imbalance
ones = data[data["Outcome"]==1].shape[0]
zeros = data[data["Outcome"]==0].shape[0]
print(ones)
print(zeros)
plt.bar(data["Outcome"].unique(), [ones,zeros], label=["Non-diabetic","Diabetic"],color=["red","blue"])
plt.xlabel(["Non-diabetic","Diabetic"])
plt.legend()


# In[31]:


x= data.drop("Outcome",axis=1)
y = data["Outcome"]


# In[32]:


x_tr, x_test, y_tr, y_test = train_test_split(x,y,test_size=0.2)


# In[33]:


# creating the input layer
input_layer = keras.Input(shape=[x.shape[1]])


# In[34]:


#hiddenlayers
hl1 = Dense(6, activation="relu")
hl1 = hl1(input_layer)


# In[35]:


hl2 = Dense(4, activation="relu")
hl2= hl2(hl1)


# In[36]:


output_layer = Dense(1, activation="relu")
output_layer= output_layer(hl2)


# In[37]:


model = keras.Model(inputs= input_layer, outputs= output_layer)


# In[38]:


model.summary()


# In[39]:


keras_earlystop = keras.callbacks.EarlyStopping(monitor="loss", mode="min", patience=3)
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(x_tr,y_tr, epochs=100, callbacks=[keras_earlystop])


# In[40]:


model.evaluate(x_tr,y_tr)


# In[41]:


p_tr = model.predict(x_tr)
p_test = model.predict(x_test)
p_test[0:10]


# In[42]:


p_list =[ 0 if i <0.5 else 1 for i in p_test ]

print(p_list)


# In[43]:


print(classification_report(y_test, p_list))
print(confusion_matrix(y_test,p_list))

