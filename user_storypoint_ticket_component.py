#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:32:46 2019

@author: neha
"""


import pandas as pd

employee_data=pd.read_csv('emp_data.csv')

username=input("Please Enter Username: ")
storypoint=int(input("Please Enter Storypoint: "))
component_val=employee_data.loc[:,"component"].unique()
component_val=list(component_val)
print("Available Components are as follows type any one",component_val)
component=input("Please Enter Component Name: ")
ticket=input("Please Enter Ticket Type: ")
df=employee_data.loc[employee_data['Username'] == username]
df.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)

if ticket=='modification':
  ticket=0
elif ticket=='bugs':
    ticket=1
else:
    ticket=2
component_data=df.loc[:,"component"].unique()

print(len(component_data))
a=list(range(0,len(component_data)))
df.component.replace(component_data, a, inplace=True)
component_data=list(component_data)
for i in component_data:

  if i==component:
      print("found")
      print(component_data.index(i))
      index=component_data.index(i)
  else:
      for i in component_val:
           if component==i:
              index=component_val.index(i)



storypoint_data=df.columns[1]
component_values=df.columns[6]
ticket_values=df.columns[4]

features =[]
features.append(storypoint_data)
features.append(component_values)
features.append(ticket_values)

print(features)

y = df["effort"]
X = df[features]
#print(y)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)

print(lin.predict([[storypoint,index,ticket]]))
print("{} can do work in {} hours".format(username,lin.predict([[storypoint,index,ticket]])[0]))







