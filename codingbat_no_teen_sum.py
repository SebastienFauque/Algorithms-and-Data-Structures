#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:18:43 2020

@author: sebastien
@title: codingbat_no_teen_sum.py

Given 3 int values, a b c, return their sum. However, if any 
of the values is a teen -- in the range 13..19 
inclusive -- then that value counts as 0, except 15 and 
16 do not count as a teens. Write a separate helper 
"def fix_teen(n):"that takes in an int value and returns 
that value fixed for the teen rule. In this way, you avoid 
repeating the teen code 3 times (i.e. "decomposition"). Define
 the helper below and at the same indent level as the 
 main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

"""

def no_teen_sum(a, b, c):
  total = 0
  mylist = [a, b, c]
  for i in mylist:
    if i in range(13, 20):
      total += fix_teen(i)
    else:
      total += i
  
  return total
  
def fix_teen(n):
  if n == 15 or n == 16:
    return n
  else:
    return 0

a = 2
b = 15
c = 13

print(no_teen_sum(a,b,c))
