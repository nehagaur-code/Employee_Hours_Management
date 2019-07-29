#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:06:42 2019

@author: neha
"""


import pandas as pd

employee_data=pd.read_csv('emp_data.csv')

username=input("Please Enter Username: ")
tickettype=input("Please Enter Ticket Type: ")
component_val=employee_data.loc[:,"component"].unique()
component_val=list(component_val)
print("Available Components are as follows type any one",component_val)
component=input("Please Enter Component Name: ")
module=input("Please Enter Module Name: ")
df=employee_data.loc[employee_data['Username'] == username]
df.module.replace(['ui', 'frontend','backend'], [0,1,2], inplace=True)
df.tickettype.replace(['modification', 'bugs','new requirement'], [0,1,2], inplace=True)

if module=='ui':
  module=0
elif module=='frontend':
    module=1
else:
    module=2
    
    
    

if tickettype=='modification':
  tickettype=0
elif tickettype=='bugs':
    tickettype=1
else:
    tickettype=2
    
    
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



tickettype_data=df.columns[4]
component_values=df.columns[6]
module_data=df.columns[5]

features =[]
features.append(tickettype_data)
features.append(component_values)
features.append(module_data)

print(features)

y = df["effort"]
X = df[features]
#print(y)
from sklearn.linear_model import LinearRegression 
lin = LinearRegression() 
lin.fit(X, y)

print(lin.predict([[tickettype,index,module]]))
print("{} can do work in {} hours".format(username,lin.predict([[tickettype,index,module]])[0]))




