#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:55:08 2020

@author: sebastien
@title: codingbat_close_far.py

Given three ints, a b c, return True if one of b or c 
is "close" (differing from a by at most 1), while the 
other is "far", differing from both other values by 2 
or more. Note: abs(num) computes the absolute value of 
a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""

def close_far(a, b, c): # 4, 1, 3
  ab = abs(a-b) 
  ac = abs(a-c) 
  bc = abs(b-c) 
  
  total_list = [ab, ac, bc]
  
  close = 0
  far = 0
  for i in total_list:
      if i >= 2:
          far += 1
      else:
          close += 1
         
  if far == 2 and close == 1:
      return True
  else:
      return False

a = 1
b = 2
c = 10
print(close_far(a,b,c))