#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:55:24 2019

@author: neha
"""

#calculte effort based on user and storypoint


import pandas as pd
import numpy as np

employee_data=pd.read_csv('emp_data.csv')

#some_value="user1"
username=input("Please Enter Username: ")
storypoint=int(input("Please Enter Storypoint: "))
df=employee_data.loc[employee_data['Username'] == username]


features = list(df.columns[1:2])

y = df["effort"]
X = df[features]
#print(y)
Y = pd.get_dummies(data=y, drop_first=True)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)

print(lin.predict([[storypoint]]))
print("{} can do work in {} hours".format(username,lin.predict([[storypoint]])[0]))
