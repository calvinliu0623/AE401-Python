# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:21:25 2020

@author: CALVIN
"""


num=int(input("班上人數:"))
slist=[]
for i in range(num):
    score=int(input("成績")
    name=input("名字")
    slist.append(score)
    slist.append(name)
def ave (slist):
    t=0
    for j in range(0,num*2,2):
        t=t+(slist[j])
    return t
def maxx (slist):
    maxxx=0
    for j in range(0,num*2,2):
        if slist[j]>=maxxx:
            maxxx=slist[j]
            maxxname=slist[j+1]
    print("最高分分數:",maxxx)
    print("最高分名字:",maxxname)
def minn (slist):
    minnn=100
    for j in range(0,num*2,2):
        if slist[j]<=minnn:
            minnn=slist[j]
            minnname=slist[j+1]
    print("最低分分數:",minnn)
    print("最低分名字:",minnname)
tt=ave(slist)
print("平均:",tt)
maxx(slist)
minn(slist)