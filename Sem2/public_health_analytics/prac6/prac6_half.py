#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


data = pd.read_csv("METABRIC_RNA_Mutation.csv")
data.head()


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[10]:


data.shape


# In[11]:


data.describe()


# In[12]:


data["cancer_type"].unique()


# In[13]:


data["type_of_breast_surgery"].unique()


# In[14]:


data = data.dropna(subset=["type_of_breast_surgery"])
data.shape


# In[15]:


na = data.isna().sum()
na


# In[16]:


na[na >0].sort_values(ascending=False)


# In[17]:


num_col = data.select_dtypes("number")
print(num_col.columns)
num_col


# In[18]:


plt.hist(data["age_at_diagnosis"], density=True, bins=50, edgecolor="black")


# In[19]:


plt.boxplot([data["age_at_diagnosis"]])


# In[20]:


data.boxplot(column="age_at_diagnosis", by="death_from_cancer", grid=False)


# In[21]:


data.boxplot(column="age_at_diagnosis", by="chemotherapy", grid=False)


# In[22]:


data.boxplot(column="age_at_diagnosis", by="hormone_therapy", grid=False)


# In[23]:


plt.hist(data["overall_survival_months"], density=True, bins=30, color="purple", edgecolor="black")


# In[24]:


data.boxplot(column="overall_survival_months", by="death_from_cancer", grid=False)


# In[25]:


data.boxplot(column="overall_survival_months", by="chemotherapy", grid=False)


# In[26]:


data.boxplot(column="overall_survival_months", by="hormone_therapy", grid=False)


# In[27]:


plt.hist(data["tumor_size"], bins=40, density=True)


# In[28]:


corr= num_col[["age_at_diagnosis", "neoplasm_histologic_grade", "lymph_nodes_examined_positive", "overall_survival_months"]].corr()
corr.columns


# In[29]:


plt.figure(figsize=(10,10))
plt.imshow(corr,cmap="coolwarm")

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        value = corr.iloc[i, j]
        plt.text(j, i, f"{value:.2f}", ha='center', va='center', color='black')
plt.xticks(ticks=np.arange(len(corr.columns)), labels=corr.columns, rotation=90, ha='right')
plt.yticks(ticks=np.arange(len(corr.columns)), labels=corr.columns)


# In[30]:


import seaborn as sns


sns.countplot(x="tumor_stage", data=data, hue="death_from_cancer")


# In[31]:


avg_tumor_size_by_death_status = data.groupby("death_from_cancer")["tumor_size"].mean()
avg_tumor_size_by_death_status
plt.bar(height=avg_tumor_size_by_death_status, x=avg_tumor_size_by_death_status.index)


# In[32]:


data.groupby("death_from_cancer")["tumor_size"].describe()


# In[33]:


sns.scatterplot(data=data, x="tumor_size", y="age_at_diagnosis", hue="death_from_cancer")


# In[34]:


sns.scatterplot(data=data, x="tumor_size", y="overall_survival_months", hue="death_from_cancer")


# In[49]:


val =[word for word in data.columns if word.startswith("cd")]


# In[50]:


subset1= data.loc[:, ["death_from_cancer", "cdkn1a","tumor_stage"]]
subset1.sort_values(by="cdkn1a",ascending =False)


# In[51]:


subset1.groupby("tumor_stage")["cdkn1a"].mean()


# In[52]:


data = data.dropna()


# In[53]:


data.shape


# In[55]:


data.isna().sum()[0:10]


# In[56]:


x= data.drop("death_from_cancer", axis=1)
y= data["death_from_cancer"]


# In[57]:


cat_df= x.select_dtypes(include="object")
cat_df.columns


# In[59]:


data_encoded = pd.get_dummies(columns=cat_df.columns,data=x)
data_encoded.head()


# In[62]:


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# In[69]:


x_tr, x_test, y_tr,y_test = train_test_split(data_encoded,y, test_size=0.2, random_state=10)


# In[70]:


logit1=LogisticRegression().fit(x_tr,y_tr)
pred_tr_logit1=logit1.predict(x_tr)
print(classification_report(y_tr,pred_tr_logit1))


# In[71]:


pred_test_logit1= logit1.predict(x_test)
print(classification_report(y_test, pred_test_logit1))


# # Decision Tree

# In[74]:


treeModel = DecisionTreeClassifier().fit(x_tr,y_tr)
predTree = treeModel.predict(x_tr)
print(classification_report(y_tr, predTree))
print(classification_report(y_test, treeModel.predict(x_test)))


# # Random Forest

# In[76]:


rfModel = RandomForestClassifier().fit(x_tr,y_tr)


# In[77]:


rfPredTrain = rfModel.predict(x_tr)
rfPredTest = rfModel.predict(x_test)
print(classification_report(y_tr,rfPredTrain))
print(classification_report(y_test,rfPredTest))


# ## Grid search CV for selecting best columns

# In[81]:


from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline


# In[82]:


param={"kbest__k": [10,20,30,40,50,100,200,400,1000,2000,4000,5000]}


# In[84]:


rfClassifier=RandomForestClassifier()
featureSel = SelectKBest(f_classif)


# In[89]:


gdModel = GridSearchCV(Pipeline([('kbest', featureSel),('classify',rfClassifier)]),param_grid=param,cv=10)


# In[90]:


gdModel.fit(data_encoded, y)


# In[91]:


gdModel.best_params_


# In[93]:


bestFeature = SelectKBest(f_classif, k=20).fit(data_encoded,y)


# In[94]:


bestCols =bestFeature.get_support(indices=True)


# In[95]:


data_encoded.iloc[:, bestCols].head()


# In[96]:


x_new = SelectKBest(f_classif,k=20).fit_transform(data_encoded,y)


# In[97]:


x_new.shape


# In[98]:


x_tr, x_test, y_tr, y_test = train_test_split(x_new, y, test_size=0.2, random_state=100)


# In[99]:


rfModel2= RandomForestClassifier(n_estimators=500).fit(x_tr,y_tr)


# In[100]:


rfPredTrain = rfModel2.predict(x_tr)
rfPredTest = rfModel2.predict(x_test)


# In[101]:


print(classification_report(y_tr, rfPredTrain))
print(classification_report(y_test, rfPredTest))


# In[ ]:




