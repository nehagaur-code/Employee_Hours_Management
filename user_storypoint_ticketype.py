#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:15:12 2019

@author: neha
"""

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
#y=employee_data["Username"]

username=input("Please Enter Username: ")
storypoint=int(input("Please Enter Storypoint: "))
tickettype=input("Please Enter Ticket type: ")
tickettype=tickettype.lower()


df=employee_data.loc[employee_data['Username'] == username]





df.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)

if tickettype=='modification':
  tickettype=0
elif tickettype=='bugs':
    tickettype=1
else:
    tickettype=2



storypoint_data=df.columns[1]
tickettype_data=df.columns[4]



features =[]
features.append(storypoint_data)
features.append(tickettype_data)
print(features)

y = df["effort"]
X = df[features]
#print(y)
X = pd.get_dummies(data=X, drop_first=True)
#print(X)
Y = pd.get_dummies(data=y, drop_first=True)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)
print(lin.predict([[storypoint,tickettype]]))

#print("{} can do work in {} hours".format(username,lin.predict([[storypoint]])[0]))
