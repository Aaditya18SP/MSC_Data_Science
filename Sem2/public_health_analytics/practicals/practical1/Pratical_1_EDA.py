#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[105]:


data = pd.read_csv("inpatientCharges.csv")
data.head()


# In[106]:


data.columns


# In[107]:


data [["State_name", "Region"]] = data["Hospital Referral Region Description"].str.split(" - ", expand= True)
data[["DRG_code","Procedure_name"]] = data["DRG Definition"].str.split(" - ", expand=True)

data= data.drop("State_name", axis=1)
data.head()


# In[108]:


data[" Average Covered Charges "] = data[" Average Covered Charges "].str.lstrip("$")
data[" Average Total Payments "] = data[" Average Total Payments "].str.lstrip("$")
data["Average Medicare Payments"] = data["Average Medicare Payments"].str.lstrip("$")

data = data.astype({"Average Medicare Payments": "float32", " Average Total Payments ": "float32", " Average Covered Charges ":"float32"})

data.head()


# In[109]:


# top 5 expensive procedures
data.groupby("Procedure_name")[" Average Covered Charges "].sum().sort_values(ascending=False).head(5)


# In[110]:


# no of procedures as per region
proc_region = data.groupby("Region")["Provider Id"].count().head(30)
plt.figure(figsize=(15,6))
plt.bar(proc_region.index,proc_region.values)
plt.tick_params(axis="x", labelrotation=90)
plt.show()


# In[111]:


# citywise average total payments
city_pay = data.groupby("Provider City")[" Average Total Payments "].mean().head(20)
#print(city_pay)
plt.figure(figsize=(15,6))
plt.bar(city_pay.index, city_pay.values)
plt.tick_params(axis="x", labelrotation=90)
plt.show()


# In[112]:


# top 5 cities with highest covered charges
city_charges = data.groupby("Provider City")[" Average Covered Charges "].sum().sort_values(ascending=False).head(5)
city_charges

plt.figure(figsize=(15,6))
plt.pie(city_charges.values, labels=city_charges.index, autopct="%1.1f%%")
plt.show()


# In[113]:


# Statewise average covered charges vs average medicare payments

avg_charges = data.groupby("Provider State")[[" Average Covered Charges ", "Average Medicare Payments"]].mean()

plt.figure(figsize=(15,6))
plt.bar(avg_charges.index,avg_charges[" Average Covered Charges "],width=0.5)
plt.bar(avg_charges.index,avg_charges["Average Medicare Payments"],width=0.5)
plt.tick_params(axis="x",labelrotation=90)
plt.show()

# experimentation
# numeric = np.arange(len(avg_charges.index))
# plt.figure(figsize=(15,6))
# plt.bar(numeric - 0.2,avg_charges[" Average Covered Charges "], width = 0.4)
# plt.bar(numeric + 0.2,avg_charges["Average Medicare Payments"], width =0.4)
# plt.tick_params(axis="x",labelrotation=90)
# plt.show()

