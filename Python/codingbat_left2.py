#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:45:26 2020

@author: sebastien
@title:codingbat_left2.py
"""

def left2(str):
    return str[2:]+str[:2]

str = 'hello'
print(left2(str))
