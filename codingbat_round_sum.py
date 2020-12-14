#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:34:15 2020

@author: sebastien
@title: codingbat_round_sum.py

For this problem, we'll round an int value up to the next 
multiple of 10 if its rightmost digit is 5 or more, so 15 
rounds up to 20. Alternately, round down to the previous 
multiple of 10 if its rightmost digit is less than 5, so 12 
rounds down to 10. Given 3 ints, a b c, return the sum of their
 rounded values. To avoid code repetition, write a separate 
 helper "def round10(num):" and call it 3 times. Write the 
 helper entirely below and at the same indent level as 
 round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10

"""

def round_sum(a, b, c):
  total = 0
  intlist = [a, b, c]
  
  for i in intlist:
    total += round10(i)
  
  return total
  
def round10(num):
  numstr = str(num)
  lenstr = len(numstr)
  lastdig = numstr[-1]
  int_last_dig = int(lastdig)
  ret_num = 0
  
  if lenstr == 1:
    if num >= 5:
      return 10
    else:
      return 0
  elif lenstr > 1:
    if int_last_dig >= 5:
      ret_num = num - int_last_dig + 10
      return ret_num
    else:
      ret_num = num - int_last_dig
      return ret_num
      
  

a = 23
b = 11
c = 26
print(round_sum(a, b, c))