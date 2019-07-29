#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:13:20 2019

@author: neha
"""


import pandas as pd
import numpy as np
features=[]
employee_data=pd.read_csv('emp_data.csv')
#y=employee_data["Username"]

username=input("Please Enter Username: ")
storypoint=int(input("Please Enter Storypoint: "))
modulename=input("Please Enter ModuleName: ")
tickettype=input("Please Enter Ticket type: ")
modulename=modulename.lower()
tickettype=tickettype.lower()

df=employee_data.loc[employee_data['Username'] == username]





df.module.replace(['ui', 'frontend','backend'], [0,1,2], inplace=True)
df.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)

storypoint_name=df.columns[1]
module=df.columns[5]
tickettype_name=df.columns[4]





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



features.append(storypoint_name)
features.append(module)
features.append(tickettype_name)
print(features)

y = df["effort"]
X = df[features]
X = pd.get_dummies(data=X, drop_first=True)
Y = pd.get_dummies(data=y, drop_first=True)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)
print(lin.predict([[storypoint,modulename,tickettype]]))

print("{} can do work in {} hours".format(username,lin.predict([[storypoint,modulename,tickettype]])[0]))
