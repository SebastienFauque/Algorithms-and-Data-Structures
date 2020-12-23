#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:56:38 2020

@author: sebastien
@title: codingbat_make_bricks.py
"""


def make_bricks(small, big, goal):
  #  case: less than goal
  if ((1 * small) + (5 * big)) < goal:
    return False
  #  case: equal to goal
  elif ((1 * small) + (5 * big)) == goal:
    return True
  #  case: greater than goal  
  else:
    #  see if small is able to get to the last digit of goal
    str_goal = str(goal)
    last_goal = str_goal[-1]
    if small >= int(last_goal):
      return True
    elif int(last_goal) > 5:
      if small >= (int(last_goal) - 5):
        return True
    if int(last_goal) == 0 or int(last_goal) == 5:
        return True
    else:
      return False
  
small = 3  #0
big = 8  #100
goal = 8  #1

print(make_bricks(small, big, goal))
