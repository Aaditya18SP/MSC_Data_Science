#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from wordcloud import WordCloud


# In[3]:


data = pd.read_csv("./data.csv")
data.head()


# In[4]:


data.columns


# In[5]:


data =data.drop("Unnamed: 0", axis=1)
data.head()


# In[6]:


nltk_download_dir="/home/aadityapal/.conda/envs/notebook/nltk_data"


# In[7]:


nltk.download("punkt_tab",download_dir=nltk_download_dir)


# In[8]:


data["status"].value_counts()


# In[9]:


data.isna().sum()


# In[10]:


data = data.dropna()


# # Tokenizer

# In[11]:


word_list =[]
for word in data["statement"]:
    word_list.append(word_tokenize(word))

data["word"]=word_list
data.head()


# ## remove punctuation

# In[12]:


no_punct=[]
for word in data["statement"]:
    no_punct.append(RegexpTokenizer("[A-Z]|[a-z]+").tokenize(word.lower()))
data["no_punct_word"]=no_punct
data.head()


# In[13]:


nltk.download("stopwords", download_dir=nltk_download_dir)


# In[ ]:


no_stop_words = []
for wordArr in data["no_punct_word"]:
    currentRow=[]
    for word in wordArr:
        if word not in stopwords.words("english"):
            currentRow.append(word)
    no_stop_words.append(currentRow)
data["no_stopword"]=no_stop_words
data.head()


# In[ ]:


#lemmatization


# In[ ]:


nltk.download("wordnet", download_dir=nltk_download_dir)


# In[ ]:


word_lemma=[]
for wordArr in data["no_stopword"]:
    row=[]
    for word in wordArr:
        row.append(WordNetLemmatizer().lemmatize(word))
    word_lemma.append(row)
data["word_lemma"]=word_lemma
data.head()


# In[ ]:


nltk.download("averaged_perceptron_tagger_eng", download_dir=nltk_download_dir)


# In[ ]:


word_tag =[]
for wordArr in data["word_lemma"]:
    word_tag.append(nltk.pos_tag(wordArr))
data["pos_tag"]= word_tag
data.head()


# In[ ]:


noun_tag=[]
for wordArr in data["pos_tag"]:
    pos_row=[]
    for (word,pos) in wordArr:
        if pos.startswith("NN"):
            pos_row.append(word)
    noun_tag.append(pos_row)
data["noun_tag"]= noun_tag
data.head()


# In[ ]:


## generate word cloud


# In[ ]:


wordList =data["noun_tag"].map(lambda x : ",".join(x))
print(wordList)
words=",".join(wordList)
#words


# In[ ]:


wc= WordCloud(background_color="black", max_words=5000, contour_color="blue")
wc.generate(words)


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


plt.figure(figsize=(50,50))
wc.to_image()


# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer


# In[ ]:


v1= CountVectorizer().fit_transform(wordList)
v1.toarray()


# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[ ]:


x_tr,x_test, y_tr, y_test = train_test_split(v1, data["status"], test_size=.2)


# In[ ]:


logit_mod=LogisticRegression().fit(x_tr, y_tr)


# In[ ]:


pred=logit_mod.predict(x_test)


# In[ ]:


from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder


# In[ ]:


print(classification_report(y_test,pred))


# In[ ]:


y=LabelEncoder().fit_transform(data["status"])
print(len(y_test))
x_tr,x_test, y_tr,y_test = train_test_split(v1, y, test_size=.2)


# In[ ]:


logit_mod2= LogisticRegression().fit(x_tr,y_tr)


# In[ ]:


p2= logit_mod2.predict_proba(x_test)
print(len(y_test))
print(len(p2))


# In[ ]:


auc=roc_auc_score(y_test, p2,multi_class="ovr")
auc


# In[ ]:




