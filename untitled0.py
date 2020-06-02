# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:30:33 2020

@author: CALVIN
"""

import random

a = random.randint(1,10)
c = 0
while True:
    guess = int(input("猜個數字1到10:"))
    if guess == a:
        print (count)
        print ("bingo!!!")
        break
    elif guess > a:
        print ("smaller")
        count + 1
    elif guess < a:
        print ("bigger")
        count + 1
    else:
        print ('wrong')
