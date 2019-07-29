#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:33:33 2019

@author: neha
"""

#storypoint and component

import pandas as pd
import numpy as np

employee_data=pd.read_csv('emp_data.csv')
component_data=employee_data.loc[:,"component"].unique()

a=list(range(0,len(component_data)))
storypoint=employee_data.columns[1]
employee_data.component.replace(component_data, a, inplace=True)
component=employee_data.columns[6]
features =[]
features.append(storypoint)
features.append(component)
print(features)

y = employee_data["effort"]
X = employee_data[features]

from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)
print(lin.predict([[2,2]]))