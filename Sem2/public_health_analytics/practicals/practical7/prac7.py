#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


import warnings
warnings.simplefilter("ignore")


# In[4]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[5]:


df=pd.read_csv("../prac6/METABRIC_RNA_Mutation.csv" )


# In[6]:


df.head()


# In[7]:


#process of selecting x consisting of mutated gene expressions


# In[8]:


df.dtypes.index


# In[12]:


df_mutated_genes=df.loc[:, ["death_from_cancer","mtap_mut", "ppp2cb_mut",'hras_mut', "prps2_mut","nras_mut", "ndfip1_mut","smarcd1_mut", "smarcb1_mut", "stmn2_mut", "siah1_mut"]]


# In[13]:


df_mutated_genes.head()


# In[14]:


df_mutated_genes.dtypes


# In[15]:


df_mutated_genes.isna().sum()


# In[16]:


from sklearn.feature_selection import SelectKBest,f_classif


# In[17]:


x=df_mutated_genes.drop("death_from_cancer", axis=1)


# In[19]:


x=pd.get_dummies (columns=x. columns, data=x,dtype=int, drop_first=True)


# In[20]:


x.dtypes


# In[22]:


#remove duplicate columns
x = x.loc[:,~x.columns.duplicated() ].copy()


# In[23]:


x.dtypes


# In[28]:


#replace null values with "Living"
df["death_from_cancer"].fillna("Living", inplace=True)


# In[29]:


df["death_from_cancer"].value_counts()


# In[30]:


y=df["death_from_cancer" ]


# In[31]:


best_model=SelectKBest(f_classif,k=4).fit(x,y)


# In[32]:


col_bst=best_model.get_support(indices=True)


# In[33]:


col_bst


# In[34]:


x.iloc[:, col_bst].head()


# In[40]:


x_new_best=SelectKBest(f_classif, k=4).fit_transform(x,y)


# In[41]:


x_new_best.shape


# In[43]:


from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# In[46]:


x_scaled=StandardScaler().fit_transform(x_new_best)


# In[45]:


x_scaled


# In[49]:


wcss=[]
for i in range(2,6):
    model = KMeans(init="random", n_clusters=1, random_state=100).fit(x_scaled)
    wcss.append(model.inertia_)


# In[50]:


wcss


# In[52]:


plt.plot(range(2,6),wcss,marker="o",markerfacecolor="red")


# In[53]:


kmeans_final=KMeans(n_clusters=2, init="random").fit(x_scaled)


# In[54]:


clusters=kmeans_final.predict(x_scaled)


# In[55]:


clusters


# In[56]:


x["clusters"]=clusters
print(x["clusters"].value_counts())


# In[65]:


from sklearn.metrics import silhouette_score


# In[66]:


silhouette_score(x_new_best, clusters)


# In[67]:


x_new=x.iloc[:,col_bst]


# In[68]:


x_new["death_from_cancer"]=y


# In[69]:


x_new["clusters"]=clusters


# In[70]:


sns.countplot(x="clusters", hue="death_from_cancer", data=x_new)


# In[72]:


x_new[x_new.clusters==0].head()


# In[73]:


x_new["stmn2_mut_N145K_1"].value_counts()


# In[71]:


x_new[x_new.clusters==1].head()


# In[ ]:




