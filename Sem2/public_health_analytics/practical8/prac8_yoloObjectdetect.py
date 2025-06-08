#!/usr/bin/env python
# coding: utf-8

# In[37]:


from roboflow import Roboflow


# In[38]:


rf= Roboflow(api_key="Y9UjYJSYyE54rTTrYgX7")
project= rf.workspace("phamumbaiuni").project("axialmri")
version = project.version(1)
dataset= version.download("yolov5")


# In[39]:


dataset


# In[55]:


import inference
import os


# In[56]:


model = inference.get_model("axialmri/1", api_key="Y9UjYJSYyE54rTTrYgX7")


# In[57]:


testPath= os.listdir("./axialMri-1/test")
testPath


# In[64]:


validationPath = "./axialMri-1/valid/images/"


# In[65]:


validImagesPath = os.listdir(validationPath)
validImagesPath


# In[66]:


validationImagePath = validImagesPath[0]
validationImagePath


# In[67]:


validationPath+validImagesPath[0]


# In[68]:


result = model.infer(validationPath+validImagesPath[0], model_id="axialmri/1")


# In[69]:


result[0]


# In[80]:


import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


# In[101]:


plt.figure(figsize=(20,20))
j=1


# In[102]:


for imagePath in validImagesPath:
    if j>8:
        break
    plt.subplot(2,4,j)
    plt.subplots_adjust(wspace=0.5, hspace=1)
    imgpath = validationPath+imagePath
    result = model.infer(validationPath+imagePath, model_id="axialmri/1")
    if len(result[0].predictions)>0:
        im = Image.open(imgpath)
        draw_img= ImageDraw.Draw(im)
        predResult = result[0].predictions[0]
        # x1=result[0].predictions[0].x
        # y1=result[0].predictions[0].y
        x1=predResult.x
        y1= predResult.y
        width = predResult.width
        height= predResult.height
        className = predResult.class_name
        x2=x1+width
        y2=y1+height
        draw_img.rectangle([x1, y1, x2,y2], outline="red")
        plt.imshow(im)
        plt.xlabel(className)
        j+=1


# In[ ]:




