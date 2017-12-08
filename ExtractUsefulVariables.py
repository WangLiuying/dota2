
# coding: utf-8

# load and read

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


heroAbi_train = pd.read_csv('heroAbilityInGames_train.csv',encoding = 'UTF-8')
del heroAbi_train['Unnamed: 0']
heroAbi_train


# In[4]:


heroAbi_test = pd.read_csv('heroAbilityInGames_test.csv', encoding = 'UTF-8')
del heroAbi_test['Unnamed: 0']
heroAbi_test


# 队伍整体水平

# In[63]:


def extractVariables(players):
    numRadientHeroes = players.iloc[:,::27].apply('sum',axis=1)-5 #本方天辉英雄个数
    numMeleeHeroes = players.iloc[:,1::27].apply('sum',axis=1)-5#本方近战英雄个数
    meanCore = players.iloc[:,2::27].apply('mean',axis=1)
    maxCore = players.iloc[:,2::27].apply('max',axis=1)
    meanControl = players.iloc[:,3::27].apply('mean',axis=1)
    maxControl = players.iloc[:,3::27].apply('max',axis=1)
    meanInitial = players.iloc[:,4::27].apply('mean',axis=1)
    maxInitial = players.iloc[:,4::27].apply('max',axis=1)
    meanJungle = players.iloc[:,5::27].apply('mean',axis=1)
    maxJungle = players.iloc[:,5::27].apply('max',axis=1)
    meanSupport = players.iloc[:,6::27].apply('mean',axis=1)
    maxSupport = players.iloc[:,6::27].apply('max',axis=1)
    meanDurable = players.iloc[:,7::27].apply('mean',axis=1)
    maxDurable = players.iloc[:,7::27].apply('max',axis=1)
    meanExplosive = players.iloc[:,8::27].apply('mean',axis=1)
    maxExplosive = players.iloc[:,8::27].apply('max',axis=1)
    meanPush = players.iloc[:,9::27].apply('mean',axis=1)
    maxPush = players.iloc[:,9::27].apply('max',axis=1)
    meanSurvive = players.iloc[:,10::27].apply('mean',axis=1)
    maxSurvive = players.iloc[:,10::27].apply('max',axis=1)
    meanStrength = pd.Series(np.apply_along_axis(func1d=np.mean,axis=1,arr=(np.array(players.iloc[:,11::27])+np.array(players.iloc[:,12::27])*25)))
    maxStrength = pd.Series(np.apply_along_axis(func1d=np.max,axis=1,arr=(np.array(players.iloc[:,11::27])+np.array(players.iloc[:,12::27])*25)))
    meanAgility = pd.Series(np.apply_along_axis(func1d=np.mean,axis=1,arr=(np.array(players.iloc[:,13::27])+np.array(players.iloc[:,14::27])*25)))
    maxAgility = pd.Series(np.apply_along_axis(func1d=np.max,axis=1,arr=(np.array(players.iloc[:,13::27])+np.array(players.iloc[:,14::27])*25)))
    meanWisdom = pd.Series(np.apply_along_axis(func1d=np.mean,axis=1,arr=(np.array(players.iloc[:,15::27])+np.array(players.iloc[:,16::27])*25)))
    maxWisdom = pd.Series(np.apply_along_axis(func1d=np.max,axis=1,arr=(np.array(players.iloc[:,15::27])+np.array(players.iloc[:,16::27])*25)))
    meanAttackValue = players.iloc[:,17::27].apply('mean',axis=1)
    meanAttackSpeed = players.iloc[:,18::27].apply('mean',axis=1)
    meanAttackOutput = pd.Series(np.apply_along_axis(func1d=np.mean, axis = 1, arr = np.array(players.iloc[:,17::27])*np.array(players.iloc[:,18::27])))
    meanAttackDist = players.iloc[:,19::27].apply('mean',axis=1)
    maxAttackDist = players.iloc[:,19::27].apply('max',axis=1)
    meanDefence = players.iloc[:,20::27].apply('mean',axis=1)
    maxDefence = players.iloc[:,20::27].apply('max',axis=1)
    meanPDef = players.iloc[:,21::27].apply('mean',axis=1)
    maxPDef = players.iloc[:,21::27].apply('max',axis=1)
    meanMDef = players.iloc[:,22::27].apply('mean',axis=1)
    maxMDef = players.iloc[:,22::27].apply('max',axis=1)
    meanMove = players.iloc[:,23::27].apply('mean',axis=1)
    maxMove = players.iloc[:,23::27].apply('max',axis=1)
    minMove = players.iloc[:,23::27].apply('min',axis=1)
    maxDaySight = players.iloc[:,25::27].apply('max', axis=1)
    maxNightSight = players.iloc[:,26::27].apply('max', axis=1)
    data = {'numRadientHeroes':numRadientHeroes,'numMeleeHeroes':numMeleeHeroes ,
        'meanCore':meanCore, 'maxCore':maxCore, 'meanControl':meanControl, 'maxControl':maxControl, 
        'meanInitial':meanInitial, 'maxInitial':maxInitial, 'meanJungle':meanJungle, 'maxJungle':maxJungle, 
        'meanSupport':meanSupport, 'maxSupport':maxSupport,'meanDurable':meanDurable, 'maxDurable':maxDurable, 
        'meanExplosive':meanExplosive, 'maxExplosive':maxExplosive, 'meanPush':meanPush, 'maxPush':maxPush, 
        'meanSurvive':meanSurvive, 'maxSurvive':maxSurvive,
        'meanStrength':meanStrength, 'maxStrength':maxStrength, 
        'meanAgility':meanAgility, 'maxAgility':maxAgility, 
        'meanWisdom':meanWisdom, 'maxWisdom':maxWisdom, 
        'meanAttackValue':meanAttackValue, 'meanAttackSpeed':meanAttackSpeed, 'meanAttackOutput':meanAttackOutput,
        'meanAttackDist':meanAttackDist, 'maxAttackDist':maxAttackDist,
        'meanDefence':meanDefence, 'maxDefence':maxDefence, 'meanPDef':meanPDef, 'maxPDef':maxPDef, 'meanMDef':meanMDef, 'maxMDef':maxMDef,
        'meanMove':meanMove, 'maxMove':maxMove, 'minMove':minMove,
        'maxDaySight':maxDaySight, 'maxNightSight':maxNightSight}
    columns = ['numRadientHeroes','numMeleeHeroes' ,
        'meanCore', 'maxCore', 'meanControl', 'maxControl', 
        'meanInitial', 'maxInitial', 'meanJungle', 'maxJungle', 
        'meanSupport', 'maxSupport','meanDurable', 'maxDurable', 
        'meanExplosive', 'maxExplosive', 'meanPush', 'maxPush', 
        'meanSurvive', 'maxSurvive',
        'meanStrength', 'maxStrength', 
        'meanAgility', 'maxAgility', 
        'meanWisdom', 'maxWisdom', 
        'meanAttackValue', 'meanAttackSpeed', 'meanAttackOutput',
        'meanAttackDist', 'maxAttackDist',
        'meanDefence', 'maxDefence', 'meanPDef', 'maxPDef', 'meanMDef', 'maxMDef',
        'meanMove', 'maxMove', 'minMove',
        'maxDaySight','maxNightSight']
    myOutput = pd.DataFrame(data,columns = columns)
    return myOutput


# 提取测试集

# In[77]:


radientPlayers = heroAbi_test.iloc[:,:135]
radientPlayers = extractVariables(radientPlayers)
radientPlayers.columns = [''.join(['radient_',s]) for s in list(radientPlayers.columns)]
radientPlayers


# In[78]:


direPlayers = heroAbi_test.iloc[:,135:]
direPlayers = extractVariables(direPlayers)
direPlayers.columns = [''.join(['dire_',s]) for s in list(direPlayers.columns)]
direPlayers


# In[79]:


battleArray = pd.concat([radientPlayers,direPlayers],axis=1)
battleArray


# In[80]:


battleArray.to_csv('battleArray_test.csv',index= False, encoding = 'UTF-8')


# 提取训练集

# In[81]:


radientPlayers = heroAbi_train.iloc[:,:135]
radientPlayers = extractVariables(radientPlayers)
radientPlayers.columns = [''.join(['radient_',s]) for s in list(radientPlayers.columns)]
radientPlayers


# In[82]:


direPlayers = heroAbi_train.iloc[:,135:]
direPlayers = extractVariables(direPlayers)
direPlayers.columns = [''.join(['dire_',s]) for s in list(direPlayers.columns)]
direPlayers


# In[83]:


battleArray = pd.concat([radientPlayers,direPlayers],axis=1)
battleArray


# In[84]:


battleArray.to_csv('battleArray_train.csv',index= False, encoding = 'UTF-8')

