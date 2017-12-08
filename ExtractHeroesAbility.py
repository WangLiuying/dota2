
# coding: utf-8

# In[70]:


import re
import numpy as np
import pandas as pd
import itertools


# ### 训练集联结

# In[71]:


#%%load data
heroAttrs = pd.read_csv('heroAttrsNew.csv',encoding='UTF-8')
del heroAttrs['Unnamed: 0']
dota2train = pd.read_csv('dota2Train.csv', encoding='UTF-8',header=None)
dota2test = pd.read_csv('dota2Test.csv', encoding = 'UTF-8',header= None)
#del dota2train['Unnamed: 0']
#del dota2test['Unnamed: 0']
columnName = ['win','clusterID','gameMode','gameType'] + [str(i) for i in range(113)]
dota2train.columns = columnName
dota2test.columns = columnName


# In[72]:


attackType = {u"近战":1,u"远程":2}
attackType


# In[73]:


heroAttrs = heroAttrs.replace(attackType)


# In[74]:


camp = {u"天辉":1, u"夜魇":2}
camp


# In[75]:


heroAttrs = heroAttrs.replace(camp)


# In[76]:


heroAttrs


# In[77]:



def findHeroChoosen(x):
    heroes = (x[x==1]).index.append((x[x==-1]).index).astype('int')#找出该行中的1和-1所在位置（被选择的英雄）
    heroesInf = heroAttrs.iloc[heroes, 3:-1]#从heroAttrs表中取出相应的10条英雄属性，27个属性
    heroesInf = np.array(heroesInf).ravel()#抻直成270长度的
    return tuple(heroesInf)


# In[78]:


heroChoosen=dota2train.iloc[:,4:]
heroAbilityInGames = heroChoosen.apply(findHeroChoosen,axis=1)
heroAbility = []
for row in heroAbilityInGames:
    heroAbility.append(row)        

heroAbilityInGames = pd.DataFrame(heroAbility)


# In[79]:


heroAbilityInGames


# In[80]:


heroAbilityInGames.columns


# In[81]:


Players = ["".join(['RadientHero',str(i)]) for i in range(1,6)] + ["".join(['DireHero',str(i)]) for i in range(1,6)]
Players


# In[82]:


columnNames = ["_".join([eachplayer, eachattr]) for eachplayer, eachattr in itertools.product(Players, list(heroAttrs.columns[3:-1]))]


# In[83]:


heroAbilityInGames.columns = columnNames


# In[84]:


heroAbilityInGames


# In[85]:


heroAbilityInGames.to_csv('heroAbilityInGames_train.csv', encoding = 'UTF-8')


# ### 测试集联结

# In[86]:


heroChoosen=dota2test.iloc[:,4:]
heroAbilityInGames = heroChoosen.apply(findHeroChoosen,axis=1)
heroAbility = []
for row in heroAbilityInGames:
    heroAbility.append(row)        

heroAbilityInGames = pd.DataFrame(heroAbility)
heroAbilityInGames


# In[87]:


heroAbilityInGames.columns = columnNames
heroAbilityInGames


# In[88]:


heroAbilityInGames.to_csv('heroAbilityInGames_test.csv',encoding='UTF-8')

