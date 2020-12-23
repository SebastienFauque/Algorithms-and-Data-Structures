#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:12:04 2020

@author: sebastien
@title: codingbat_make_chocolate.py


We want make a package of goal kilos of chocolate. We have 
small bars (1 kilo each) and big bars (5 kilos each). Return 
the number of small bars to use, assuming we always use big
 bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

"""
def make_chocolate(small, big, goal):
  if goal > small*1 + big*5:
    return -1
  elif goal - (big * 5) > small:
    return -1
  elif (big * 5) > goal:
    bigCtr = 0
    while (bigCtr + 1) * 5 <= goal:
      bigCtr += 1
    if bigCtr == goal:
      return 0
    elif goal - (bigCtr * 5) > small:
      return -1
    else:
      smallCtr = (goal - (bigCtr * 5))
      return smallCtr
  else:
    ctr = (goal - (big * 5))
    return ctr
          
    
small = 1000
big = 1000000
goal = 500006

print(make_chocolate(small, big, goal))
