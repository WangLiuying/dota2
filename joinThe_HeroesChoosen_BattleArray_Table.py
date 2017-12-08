
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


battleArray_train = pd.read_csv('battleArray_train.csv')
battleArray_train


# In[5]:


battleArray_test = pd.read_csv('battleArray_test.csv')
battleArray_test


# In[6]:


trainset = pd.read_csv('dota2trainNew.csv')
del trainset['Unnamed: 0']
trainset


# In[7]:


testset = pd.read_csv('dota2testNew.csv')
del testset['Unnamed: 0']
testset


# In[8]:


testset = pd.concat([testset,battleArray_test],axis=1)
testset


# In[9]:


trainset = pd.concat([trainset,battleArray_train],axis=1)
trainset


# In[12]:


trainset.to_csv('trainset.csv', encoding = 'UTF-8',index=False)


# In[13]:


testset.to_csv('testset.csv', encoding = 'UTF-8',index=False)

