# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:14:33 2017

@author: 13656
"""

import os
os.chdir('D:\DataAnalysis\Scripts\python\dota2')
import numpy as np
import pandas as pd
#%%load data
heroAttrs = pd.read_csv('heroAttrsNew.csv',encoding='UTF-8')
del heroAttrs['Unnamed: 0']
dota2train = pd.read_csv('dota2train.csv', encoding='UTF-8',header=None)
dota2test = pd.read_csv('dota2test.csv', encoding = 'UTF-8',header= None)
#del dota2train['Unnamed: 0']
#del dota2test['Unnamed: 0']
columnName = ['win','clusterID','gameMode','gameType'] + [str(i) for i in range(113)]
dota2train.columns = columnName
dota2test.columns = columnName
#heroAttrs = heroAttrs.set_index('name_ch')
#%%
def findHeroChoosen(x):
    heroes = (x[x==1]).index.append((x[x==-1]).index).astype('int')#找出该行中的1和-1所在位置（被选择的英雄）
    heroesInf = heroAttrs.iloc[heroes, 3:-1]#从heroAttrs表中取出相应的10条英雄属性，27个属性
    heroesInf = np.array(heroesInf).ravel()#抻直成270长度的
    print(heroesInf.shape)
    return tuple(heroesInf)
#%%

heroChoosen=dota2train.iloc[:3,4:]
heroAbilityInGames = heroChoosen.apply(findHeroChoosen,axis=1)
heroAbility = []
for row in heroAbilityInGames:
    heroAbility.append(row)        

pd.DataFrame(heroAbility)
