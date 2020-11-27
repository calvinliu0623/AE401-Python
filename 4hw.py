# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:57:54 2020

@author: CALVIN
"""


import turtle
a=turtle.Turtle()
bg=turtle.Screen()
bg.bgcolor('black')
a.color('red')
a.shape('turtle')
a.penup()
for i in range(1,150):
   a.stamp()
   a.forward(10+i)
   a.left(20)
   
   
turtle.done()