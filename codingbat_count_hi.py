#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:27:21 2020

@author: sebastien
@title: codingbat_count_hi.py
"""

def count_hi(str):
  counter = 0
  sub = ''
  for i in range(len(str)):
    sub = str[i:i+2]
    if sub == 'hi':
      counter += 1
  return counter


str = 'hi'
print(count_hi(str))
