#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:35:48 2019

@author: neha
"""

import pandas as pd
import numpy as np

employee_data=pd.read_csv('emp_data.csv')
print(employee_data.shape)


features = list(employee_data.columns[1:2])
print(features)

from sklearn import tree
y = employee_data["effort"]
X = employee_data[features]
#print(y)
Y = pd.get_dummies(data=y, drop_first=True)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)
print(lin.predict([[4]]))



