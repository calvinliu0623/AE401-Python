# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:01:16 2020

@author: CALVIN
"""


import random
w=random.randint(0,6)
wi=[]
ww=random.randint(0,6)
www=random.randint(0,6)

for i in range(7):
    name=input('name:')
    n=input('noun:')
    v=input('verb:')
    wi.append([name,n,v])
print(wi)
print(wi[w][0],wi[ww][2],wi[www][1])