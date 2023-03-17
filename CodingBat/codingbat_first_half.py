#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:20:46 2020

@author: sebastien
@title: codingbat_first_half.py
"""
def first_half(str):
    if len(str) % 2 == 0:
        fHalf = int(len(str)/2)
        return str[0:fHalf]
    
str ='woohoo'
print(first_half(str))
