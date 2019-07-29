#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:01:22 2019

@author: neha
"""

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
modulename=input("Please Enter ModuleName type: ")
modulename=modulename.lower()


df=employee_data.loc[employee_data['Username'] == username]





df.module.replace(['ui', 'frontend','backend'], [0,1,2], inplace=True)

if modulename=='ui':
  modulename=0
elif modulename=='frontend':
    modulename=1
else:
    modulename=2



modulename_data=df.columns[1]
modulename_data=df.columns[5]



features =[]
features.append(modulename_data)
features.append(modulename_data)
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
print(lin.predict([[storypoint,modulename]]))

print("{} can do work in {} hours".format(username,lin.predict([[storypoint,modulename]])[0]))
