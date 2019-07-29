#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:42:48 2019

@author: neha
"""

import pandas as pd

employee_data=pd.read_csv('emp_data.csv')
modulename=input("Please Enter ModuleName: ")
tickettype=input("Please Enter Ticket type: ")


if modulename=='ui':
  modulename=0
elif modulename=='frontend':
    modulename=1
else:
    modulename=2
if tickettype=='modification':
  tickettype=0
elif tickettype=='bugs':
    tickettype=1
else:
    tickettype=2



employee_data.module.replace(['ui', 'frontend','backend'], [0,1,2], inplace=True)
employee_data.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)
module=employee_data.columns[5]
tickettype_data=employee_data.columns[4]
features=[]

features.append(module)
features.append(tickettype_data)
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
print(lin.predict([[2,2]]))




