# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:47:51 2017

@author: 13656
"""

import os
os.chdir('D:\DataAnalysis\Scripts\python\dota2')

import numpy as np
import pandas as pd
import pandas.io.json
import re
#%%
heroAttrs = pd.read_csv('heroAttributes.csv')

text = open('heroMap.txt','r').read()
text = pandas.io.json.loads(text)
heroMap = pandas.io.json.json_normalize(text['heroes'],meta = ['id','name','localized_name'])
regname = [re.sub(pattern = '_',repl = " ",string = name) for name in list(heroMap['name'])]
heroMap['name']=regname

find =pd.Series([s.lower() for s in list(heroAttrs['name'])]).isin(regname)
heroAttrs['regname']=[s.lower() for s in list(heroAttrs['name'])]
heroAttrs_merged = pd.merge(heroMap[['id','name']],heroAttrs,left_on='name',right_on='regname',left_index=True)
del heroAttrs_merged['name_x']
del heroAttrs_merged['regname']
del heroAttrs_merged['Unnamed: 0']

heroAttrs_merged = heroAttrs_merged.sort_values('id')
heroAttrs_merged.to_csv('heroAttrsNew.csv',encoding='UTF-8')

#%%
heroAttrs = pd.read_csv('heroAttrsNew.csv',encoding = 'UTF-8')
heroAttrs=heroAttrs.set_index('id')
del heroAttrs['Unnamed: 0']
dota2train = pd.read_csv('dota2Train.csv',header = None)
newColumnName = ['win','clusterID','gameType','gameMode']+list(heroAttrs['name_ch'])
dota2train.columns=newColumnName

heroPick = dota2train.ix[:,4:]
pickRate = heroPick.abs().apply('mean',axis=0)
pickRate.sort()
