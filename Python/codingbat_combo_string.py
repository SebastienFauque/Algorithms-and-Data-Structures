#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:38:00 2020

@author: sebastien
@title: codingbat_combo_string.py
"""
def combo_string(a, b):
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    
    return shorter+longer+shorter

a = 'kitten'
b = 'dog'
print(combo_string(a,b))
