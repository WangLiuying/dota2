# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:24:53 2017

@author: 13656
"""

import os 
import numpy as np
import pandas as pd 
import xgboost as xgb
os.chdir('D:\DataAnalysis\Scripts\python\dota2')
#%%
trainset = pd.read_csv('trainset.csv', encoding = 'UTF-8')

testset = pd.read_csv('testset.csv', encoding = 'UTF-8')

#%%
#attackType = {u"近战":1,u"远程":2}
#trainset = trainset.replace(attackType)
#testset = testset.replace(attackType)

#camp = {u"天辉":1, u"夜魇":2}
#trainset = trainset.replace(camp)
#testset = testset.replace(camp)
#%%
#dtrain = xgb.DMatrix(data = trainset.iloc[:,1:], label = trainset.iloc[:,1],missing= float('NaN'))
#dtest = xgb.DMatrix(data = testset.iloc[:,1:], label = testset.iloc[:,1], missing = float('NaN'))

#%%
myClassifer = xgb.XGBClassifier(learning_rate = 0.2, max_depth = 4, n_estimators = 200,
                                subsample = 0.7, colsample_bytree = 0.7,seed=123)

myClassifer.fit(X = trainset.iloc[:,1:], y = trainset.iloc[:,0])

ypred_test = myClassifer.predict(data = testset.iloc[:,1:])

ypred_test


(ypred_test == np.array(testset.iloc[:,0])).mean()

#%%
myClassifer.feature_importances_
#%%svm
