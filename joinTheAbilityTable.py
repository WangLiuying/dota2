
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd


# In[19]:


heroAbility_train = pd.read_csv('heroAbilityInGames_train.csv')
del heroAbility_train['Unnamed: 0']
heroAbility_train


# In[21]:


heroAbility_test = pd.read_csv('heroAbilityInGames_test.csv')
del heroAbility_test['Unnamed: 0']
heroAbility_test


# In[22]:


trainset = pd.read_csv('dota2trainNew.csv')
del trainset['Unnamed: 0']
trainset


# In[23]:


testset = pd.read_csv('dota2testNew.csv')
del testset['Unnamed: 0']
testset


# In[24]:


testset = pd.concat([testset,heroAbility_test],axis=1)
testset


# In[25]:


trainset = pd.concat([trainset,heroAbility_train],axis=1)
trainset


# In[26]:


trainset.to_csv('trainset.csv', encoding = 'UTF-8')


# In[27]:


testset.to_csv('testset.csv', encoding = 'UTF-8')

