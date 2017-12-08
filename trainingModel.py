
# coding: utf-8

# In[1]:


import os 
import numpy as np
import pandas as pd 
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


# In[2]:


trainset = pd.read_csv('trainset.csv', encoding = 'UTF-8')
testset = pd.read_csv('testset.csv', encoding = 'UTF-8')


# In[3]:


from sklearn import preprocessing
text_encoder = preprocessing.OneHotEncoder()


# In[4]:


text_encoder.fit_transform(np.array(testset.iloc[:,1:117])+1).toarray().shape


# In[4]:


traindata = text_encoder.fit_transform(np.array(trainset.iloc[:,1:117])+1).toarray()
testdata = text_encoder.transform(np.array(testset.iloc[:,1:117])+1).toarray()


# In[5]:


traindata = pd.concat([trainset.iloc[:,0],pd.DataFrame(traindata),pd.DataFrame(np.array(trainset.iloc[:,118:159])-np.array(trainset.iloc[:,160:]))],axis=1)


testdata = pd.concat([testset.iloc[:,0],pd.DataFrame(testdata),pd.DataFrame(np.array(testset.iloc[:,118:159])-np.array(testset.iloc[:,160:]))],axis=1)


# In[51]:


traindata.shape


# In[52]:


testdata.shape


# In[4]:


myClassifer = xgb.XGBClassifier(learning_rate = 0.1, max_depth = 5, n_estimators = 300,
                                subsample = 1, colsample_bytree = 1,seed=654)

myClassifer.fit(X =trainset.iloc[:,2:117] , y = trainset.iloc[:,0])

ypred_test = myClassifer.predict(data = testset.iloc[:,2:117])

ypred_test


print((ypred_test == np.array(testset.iloc[:,0])).mean(),'\n',myClassifer.feature_importances_)


# ## naive bayes

# with extracted variables

# In[7]:


from sklearn import naive_bayes


# In[17]:


nbClf = naive_bayes.BernoulliNB(alpha=1,binarize=0.5)


# In[19]:


nbClf.fit(X=traindata.iloc[:,1:394],y=traindata.iloc[:,0])


# In[20]:


ypred_test=nbClf.predict(X=testdata.iloc[:,1:394])
(ypred_test == np.array(testset.iloc[:,0])).mean()


# without extracted variables

# In[ ]:


nbClf = naive_bayes.BernoulliNB(alpha=1,binarize=0)


# In[ ]:


nbClf.fit(X=traindata.iloc[:,4:117],y=traindata.iloc[:,0])


# In[ ]:


ypred_test=nbClf.predict(X=testdata.iloc[:,4:117])
(ypred_test == np.array(testset.iloc[:,0])).mean()


# ## logistic

# In[6]:


from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


# In[6]:


X, y = trainset.iloc[:,2:117], trainset.iloc[:,0]
X = StandardScaler().fit_transform(X)
for i, C in enumerate((10,1,0.5, 0.3,0.1, 0.01,0.001)):
    # turn down tolerance for short training time
    clf_l1_LR = LogisticRegression(C=C, penalty='l1', tol=0.001)
    clf_l2_LR = LogisticRegression(C=C, penalty='l2', tol=0.001)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)

    coef_l1_LR = clf_l1_LR.coef_.ravel()
    coef_l2_LR = clf_l2_LR.coef_.ravel()

    # coef_l1_LR contains zeros due to the
    # L1 sparsity inducing norm

    sparsity_l1_LR = np.mean(coef_l1_LR == 0) * 100
    sparsity_l2_LR = np.mean(coef_l2_LR == 0) * 100
    print("C=%.2f" % C)
    print("Sparsity with L1 penalty: %.2f%%" % sparsity_l1_LR)
    print("score with L1 penalty: %.4f" % clf_l1_LR.score(testset.iloc[:,2:117], testset.iloc[:,0]))
    print("Sparsity with L2 penalty: %.2f%%" % sparsity_l2_LR)
    print("score with L2 penalty: %.4f" % clf_l2_LR.score(testset.iloc[:,2:117], testset.iloc[:,0]))


# 随便试验一个

# In[53]:


clf = LogisticRegression(C=0.01, penalty='l2', tol=1e-6)
X, y = traindata.iloc[:,1:], traindata.iloc[:,0]
clf.fit(X,y)


# In[54]:


(clf.predict(testdata.iloc[:,1:])==np.array(testdata.iloc[:,0])).mean()


# L2选择lambda（仅原生变量）

# In[55]:


X,y = traindata.iloc[:,1:394],traindata.iloc[:,0]
tuned_parameters = {'C':np.arange(0.01,0.2,0.01),'penalty':['l2']}

clf=GridSearchCV(LogisticRegression(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(X,y)

print("Best parameters set found on development set:")
print(clf.best_params_)
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"  % (mean, std * 2, params))


# In[59]:


clf = LogisticRegression(C=0.04,penalty='l2')


# In[60]:


clf.fit(X,y)


# In[61]:


(clf.predict(testdata.iloc[:,1:394])==np.array(testdata.iloc[:,0])).mean()


# L1选择lambda(仅原生变量)

# In[62]:


X,y = traindata.iloc[:,1:394],traindata.iloc[:,0]
tuned_parameters = {'C':np.arange(0.01,0.2,0.01),'penalty':['l1']}

clf=GridSearchCV(LogisticRegression(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(X,y)

print("Best parameters set found on development set:")
print(clf.best_params_)
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"  % (mean, std * 2, params))


# In[63]:


clf = LogisticRegression(C=0.14,penalty='l1')


# In[64]:


clf.fit(X,y)


# In[65]:


(clf.predict(testdata.iloc[:,1:394])==np.array(testdata.iloc[:,0])).mean()


# In[66]:


(clf.coef_==0).sum()


# L2选择lambda（添加变量）

# In[ ]:


X,y = traindata.iloc[:,1:],traindata.iloc[:,0]
tuned_parameters = {'C':np.arange(0.01,0.2,0.01),'penalty':['l2']}

clf=GridSearchCV(LogisticRegression(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(X,y)

print("Best parameters set found on development set:")
print(clf.best_params_)
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"  % (mean, std * 2, params))


# In[8]:


clf = LogisticRegression(C=0.12,penalty='l2')


# In[10]:


X,y = traindata.iloc[:,1:],traindata.iloc[:,0]
clf.fit(X,y)


# In[11]:


(clf.predict(testdata.iloc[:,1:])==np.array(testdata.iloc[:,0])).mean()


# L1选择lambda(添加变量)

# In[ ]:


X,y = traindata.iloc[:,1:],traindata.iloc[:,0]
tuned_parameters = {'C':np.arange(0.01,0.2,0.01),'penalty':['l1']}

clf=GridSearchCV(LogisticRegression(),tuned_parameters,cv=5,scoring='accuracy')
clf.fit(X,y)

print("Best parameters set found on development set:")
print(clf.best_params_)
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"  % (mean, std * 2, params))


# In[7]:


clf = LogisticRegression(C=0.18,penalty='l1')


# In[9]:


X,y = traindata.iloc[:,1:],traindata.iloc[:,0]
clf.fit(X,y)


# In[10]:


(clf.predict(testdata.iloc[:,1:])==np.array(testdata.iloc[:,0])).mean()


# In[30]:


name = testdata.columns[1:]
name[(clf.coef_.ravel()==0)]


# In[ ]:


clf.score(X=testdata.iloc[:,1:],y=testdata.iloc[:,0])


# adaboost

# In[24]:


from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier


# In[58]:


clf = AdaBoostClassifier(n_estimators=500,learning_rate=0.6)               


# In[59]:


clf.fit(X=traindata.iloc[:,1:],y=traindata.iloc[:,0])


# In[60]:


ypred_test=clf.predict(X=testdata.iloc[:,1:])
(ypred_test == np.array(testdata.iloc[:,0])).mean()


# ---------------------

# In[21]:


result = []
for ne in range(100,600,100):
    clf = AdaBoostClassifier(n_estimators=ne,learning_rate=1)     
    clf.fit(X=traindata.iloc[:,1:],y=traindata.iloc[:,0])
    ypred_test=clf.predict(X=testdata.iloc[:,1:])
    (ypred_test == np.array(testdata.iloc[:,0])).mean()
    result.append([(ypred_test == np.array(testdata.iloc[:,0])).mean()])


# In[22]:


result

