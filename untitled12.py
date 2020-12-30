# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:30:47 2020

@author: CALVIN
"""
import os.path
num=0
dict_Eng=0
dictionary=[]

if not os.path.isfile('a.txt'):
    fo = open('a.txt', 'w')
    print('new file')

while True:
    print('1.setting')
    print('2.english to chinese')
    print('3.chinese to emglish')
    print('4.learning result')
    print('5.list of ditionary')
    print('6.leave')
    
   
    sel=input('what do you want to do???:')
    
    if sel=='1':
       num=int(input('how many word:'))
    
       position=0
       for i in range(num):
             Chi=str(input('chinese:'))
             Eng=str(input('english:'))
             
             dictionary.insert(position,Chi)                 
             dictionary.insert(position+1,Eng)
             
             position = position + 2
             
    elif sel=='2':
          input_Eng=input('english:')
         
          for i in range(len(dictionary)):                   
                   dict_word=dictionary[i]
                                                                
                   if input_Eng == dict_word:   
                      Chi_dict_word=dictionary[i-1]              
                      print('chinese:',Chi_dict_word)
                      
    elif sel=='3':
          input_Chi=input('chinese:')
         
          for i in range(len(dictionary)):                   
                   dict_word=dictionary[i]
                                                                
                   if input_Chi == dict_word:   
                      Eng_dict_word=dictionary[i+1]              
                      print('english:',Eng_dict_word)


    elif sel=='6':
          break        
              