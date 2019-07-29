#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:35:08 2019

@author: zibal
"""


import pandas as pd
import numpy as np
df=pd.read_csv('emp_data.csv')
df3=df.loc[:,"component"].unique()
print(df3)

print(len(df3))
a=list(range(0,len(df3)))
df.component.replace(df3, a, inplace=True)
df3=list(df3)
print(df3)
a=input("enter: ")
for i in df3:

  if i==a:
      print("found")
      print(df3.index(i))
      index=df3.index(i)
  