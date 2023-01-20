#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')


# In[4]:


dataset = pd.read_csv("NewsCategorizer.csv")
print(dataset.head())


# In[5]:


dataset = dataset.drop(['links'],axis="columns")


# In[6]:


dataset.shape


# In[7]:


dataset['Category'].value_counts()


# In[8]:


target_category = dataset['Category'].unique()
print(target_category)


# In[9]:


dataset['CategoryId'] = dataset['Category'].factorize()[0]
dataset.head()


# In[10]:


category = dataset[['Category', 'CategoryId']].drop_duplicates().sort_values('CategoryId')
category


# In[11]:


dataset = dataset.dropna()


# In[12]:


text = dataset["Text"]
text.head(10)


# In[13]:


category = dataset['Category']
category.head(10)


# In[14]:


pd.options.mode.chained_assignment = None  # default='warn'


# In[15]:


def remove_tags(text):
    remove = re.compile(r'')
    return re.sub(remove, '', text)
dataset['Text'] = dataset['Text'].apply(remove_tags)


# In[16]:


dataset['Text']


# In[17]:


def special_char(text):
    reviews = ''
    for x in text:
        if x.isalnum():
            reviews = reviews + x
        else:
            reviews = reviews + ' '
    return reviews
dataset['Text'] = dataset['Text'].apply(special_char)


# In[18]:


def convert_lower(text):
    return text.lower()
dataset['Text'] = dataset['Text'].apply(convert_lower)
dataset['Text'][1]


# In[19]:


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [x for x in words if x not in stop_words]
dataset['Text'] = dataset['Text'].apply(remove_stopwords)
dataset['Text'][1]


# In[20]:


def lemmatize_word(text):
    wordnet = WordNetLemmatizer()
    return " ".join([wordnet.lemmatize(word) for word in text])
dataset['Text'] = dataset['Text'].apply(lemmatize_word)
dataset['Text'][1]


# In[21]:


x = dataset['Text']
y = dataset['CategoryId']


# In[22]:


from sklearn.feature_extraction.text import CountVectorizer
x = np.array(dataset.iloc[:,1:4].values)
y = np.array(dataset.CategoryId.values)
cv = CountVectorizer(max_features = 100)
x = cv.fit_transform(dataset.Text).toarray()
print("X.shape = ",x.shape)
print("y.shape = ",y.shape)


# In[23]:


# doc=open('text.txt','r')
# with open('text.txt') as f:
#     # contents = f.readlines()
#     contents=f.read().rstrip()
    
# contents=cv.transform([contents])


# In[ ]:





# In[24]:


import pickle
if __name__ == "__main__":
    # load the saved model (after training)
    model = pickle.load(open("categorization.model", "rb"))
    y_pred1 = cv.fit_transform(['''worldcom ex-boss launches defence lawyers defending former worldcom chief bernie ebbers against a battery of fraud charges have called a company whistleblower as their first witness.  cynthia cooper  worldcom s ex-head of internal accounting  alerted directors to irregular accounting practices at the us telecoms giant in 2002. her warnings led to the collapse of the firm following the discovery of an $11bn (Â£5.7bn) accounting fraud. mr ebbers has pleaded not guilty to charges of fraud and conspiracy.  prosecution lawyers have argued that mr ebbers orchestrated a series of accounting tricks at worldcom  ordering employees to hide expenses and inflate revenues to meet wall street earnings estimates. but ms cooper  who now runs her own consulting business  told a jury in new york on wednesday that external auditors arthur andersen had approved worldcom s accounting in early 2001 and 2002. she said andersen had given a  green light  to the procedures and practices used by worldcom. mr ebber s lawyers have said he was unaware of the fraud  arguing that auditors did not alert him to any problems.  ms cooper also said that during shareholder meetings mr ebbers often passed over technical questions to the company s finance chief  giving only  brief  answers himself. the prosecution s star witness  former worldcom financial chief scott sullivan  has said that mr ebbers ordered accounting adjustments at the firm  telling him to  hit our books . however  ms cooper said mr sullivan had not mentioned  anything uncomfortable  about worldcom s accounting during a 2001 audit committee meeting. mr ebbers could face a jail sentence of 85 years if convicted of all the charges he is facing. worldcom emerged from bankruptcy protection in 2004  and is now known as mci. last week  mci agreed to a buyout by verizon communications in a deal valued at $6.75bn.
'''])
    yy = model.predict(y_pred1)
    result = ""
    if yy == [0]:
        result = "Wellness"
    elif yy == [1]:
        result = "Politics"
    elif yy == [2]:
        result = "Entertainment"
    elif yy == [3]:
        result = "Travel"
    elif yy == [4]:
        result = "Style & Beauty"
    elif yy == [5]:
        result = "Parenting"
    elif yy == [6]:
        result = "Food & Drink"
    elif yy == [7]:
        result = "World News"
    elif yy == [8]:
        result = "Business"
    elif yy == [9]:
        result = "Sports"
    print(result)


# In[ ]:




