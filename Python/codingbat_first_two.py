#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:18:44 2020

@author: sebastien
@title: codingbat_first_two.py
"""
def first_two(str):
    if len(str) < 2:
        return str
    else: 
        return str[0:2]
    
str = 'hello'
print(first_two(str))
