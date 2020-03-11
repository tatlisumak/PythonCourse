#!/usr/bin/env python
# coding: utf-8

# In[247]:


import numpy as np
import pandas as pd
import scipy.stats 





def lin_regr(df):
    df.dropna()
    ones = pd.DataFrame(np.ones(len(df),dtype=int))
    Y = df.iloc[:,0]
    Y = Y[:,np.newaxis]
    X = df.iloc[:,1:]
    X = pd.concat((ones,X),axis=1)
    X_t_X=np.dot(X.T,X)
    X_t_X_inv =np.linalg.inv(X_t_X)
    X_t_Y = np.dot(X.T,Y)
    B = np.dot(X_t_X_inv,X_t_Y)
    
    y = B[0][0]
    for i in range(1,len(B)):
        y+= (B[i][0] * X.iloc[:,i])
    y = y[:,np.newaxis]
    
    E = Y - y
    n = len(df2)
    k = len(X.columns)-1
    sigma_square = np.dot(E.T,E)/n-k-1
    var_b = sigma_square * X_t_X_inv
    var_b = np.diag(var_b)

    std_errors = np.sqrt(var_b)[:,np.newaxis]
    
    CI = np.array([np.array(B[0] - (np.full((len(B[0]),1),1.96) * std_errors[0]))[0][0], np.array(B[0] + (np.full((len(B[0]),1),1.96) * std_errors[0]))[0][0]])

    for i in range(1,len(B)):
        CI = np.vstack((CI,np.array([np.array(B[i] - (np.full((len(B[i]),1),1.96) * std_errors[i]))[0][0], np.array(B[i] + (np.full((len(B[i]),1),1.96) * std_errors[i]))[0][0]])))
    print(f"Betas:\n{B}")
    print(f"Std. Errors:\n {std_errors}")
    print(f"Confidence Intervals 95 %:\n {CI}")


