#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[5]:


import os
import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[28]:


data_dir = "/kaggle/input/bone-fracture-detection-using-xrays/archive (6)"
train_dir = data_dir+"/train"
test_dir = data_dir+"/val"
os.listdir(data_dir)


# In[6]:


an_image = cv.imread(train_dir + "/fractured/10-rotated1.jpg")
plt.imshow(an_image)


# In[7]:


import tensorflow as tf
from tensorflow import keras


# In[8]:


train,test=keras.utils.image_dataset_from_directory( 
data_dir, 
subset="both", 
validation_split=0.2, 
batch_size=32, 
image_size=(32,32), 
seed=100, 
labels="inferred", 
class_names=["fractured", "not fractured"] 
)


# In[13]:


data_batch=train.as_numpy_iterator()


# In[14]:


batch1=data_batch.next() 


# In[15]:


len(batch1[0])


# In[16]:


batch1[0][0] 


# In[17]:


batch1[1][1]


# In[18]:


batch1[1][0]


# In[19]:


class_names = ["fractured", "not fractured"]
plt.figure(figsize=(10,10))
for i in range(0,32):
    plt.subplot(8,4,i+1)
    plt.subplots_adjust(wspace=0.2, hspace=0.9) 
    plt.imshow(batch1[0][i]/255) 
    plt.xlabel(class_names[batch1[1][i]]) 


# In[24]:


from keras import layers, models
from keras.layers import Conv2D, Dense, MaxPooling2D


# In[25]:


model=models.Sequential() 
model.add(layers.Conv2D (32, (3,3), activation='relu',input_shape=(32,32,3))) 
model.add(MaxPooling2D (pool_size=(2, 2))) 
model.add(Conv2D (64, (3, 3), activation="relu")) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Conv2D(64, (3, 3), activation="relu")) 
#model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(layers. Flatten()) 
model.add(Dense (64, activation="relu")) 
model.add(Dense (3, activation="softmax")) 
model.summary()


# In[29]:


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train, epochs=50, validation_data=test) 


# In[32]:


import pickle
f=open("/kaggle/working/model.pk1","wb") 
pickle.dump(model, f) 
f=open("/kaggle/working/model.pk1", "rb") 
model2 = pickle.load(f)
model2


# In[33]:


len(os.listdir(test_dir+"/fractured")) + len(os.listdir(test_dir+"/not fractured"))


# In[34]:


batch_test=keras.utils.image_dataset_from_directory( 
test_dir,
image_size=(32,32), 
labels=None, 
batch_size=40 
)

batch_test


# In[35]:


batch_test=batch_test.as_numpy_iterator() 
batch_test1=batch_test.next() 


# In[36]:


pred=model2.predict(batch_test1/255) 
pred



# In[37]:


pred[0]


# In[38]:


np.argmax(pred[0])


# In[39]:


pred_test =[]
for i in pred:
    pred_test.append(np.argmax(i))


# In[40]:


print(len(pred_test))
pred_test


# In[ ]:




