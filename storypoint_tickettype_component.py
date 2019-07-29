#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:25:01 2019

@author: neha
"""


import pandas as pd

employee_data=pd.read_csv('emp_data.csv')
employee_data.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)
component_data=employee_data.loc[:,"component"].unique()

a=list(range(0,len(component_data)))
storypoint=employee_data.columns[1]
employee_data.component.replace(component_data, a, inplace=True)
component=employee_data.columns[6]
tickettype=employee_data.columns[4]

features =[]
features.append(storypoint)
features.append(tickettype)
features.append(component)

y = employee_data["effort"]
X = employee_data[features]

from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)
print(lin.predict([[2,2,2]]))