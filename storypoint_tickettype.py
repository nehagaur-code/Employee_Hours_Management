#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:58:52 2019

@author: neha
"""

import pandas as pd
import numpy as np

employee_data=pd.read_csv('emp_data.csv')

employee_data.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)

storypoint=employee_data.columns[1]
tickettype=employee_data.columns[4]





features =[]
features.append(storypoint)
features.append(tickettype)
print(features)

y = employee_data["effort"]
X = employee_data[features]
#print(y)
X = pd.get_dummies(data=X, drop_first=True)
#print(X)
Y = pd.get_dummies(data=y, drop_first=True)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)
print(lin.predict([[4,2]]))





