# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:56:55 2020

@author: CALVIN
"""

scorelist=[]
people=input('people:')  

def gradefunction ():
    for i in range(int(people)):
        name=input('name:')
        grade=input('score:')
        scorelist.append(name) 
        scorelist.append(int(grade))
    return scorelist

def avgfunction (scorelist):
    total=0
    for k in range(1,int(people)*2,2):
        total=total+scorelist[k]
    avg=total/int(people)
    print('avg:',avg)

def scorefunction ():
    highest=0
    lowest=100
    for k in range(1,int(people)*2,2):
        if int(scorelist)>highest:
            highest=int(scorelist)
        if int(3,scorelist)<lowest:
            lowest=int(scorelist)
    print('highest:',highest)
    print('lowest:',lowest)
    

scorelist = gradefunction()
avgfunction(scorelist)