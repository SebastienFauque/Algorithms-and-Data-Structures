#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:53:04 2020

@author: sebastien
@title: codingbat_last2.py

"""

def last2(str):
    #  initialize the temp
    temp = ''
    
    #  initialize the search term
    item = str[-2:]
    
    #  Counter for item appears in string
    ctr = 0
    
    #  make temp a list containing two consecutive letters from str
    for letter in str:
        temp += letter
        
        #  reduce length of temp to just 2 letters
        if len(temp) > 2:
            temp = temp[1:]

        
        #  compare temp to str
        if item == temp:
            ctr += 1
    #  Empty string case
    if str == '':
        ctr += 1
        
    return ctr - 1
    
    
str = '' 
print(last2(str))