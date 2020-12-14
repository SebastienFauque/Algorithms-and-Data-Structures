#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:01:56 2020

@author: sebastien
@title: codingbat_lone_sum.py


Given 3 int values, a b c, return their sum. However, 
if one of the values is the same as another of the 
values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""



def lone_sum(a, b, c):
  sum = a + b + c
  if a == b or a == c:
    sum -= a
    
  if b == a or b == c:
    sum -= b
  
  if c == a or c == b:
    sum -= c
    
  return sum

a = 5
b = 3
c = 3
print(lone_sum(a, b, c))