#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:52:59 2020

@author: sebastien
@title: codingbat_xyz_there.py
@link: https://codingbat.com/prob/p149391

@problem: Return True if the given string contains an appearance 
of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" 
counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

"""

def xyz_there(str):
  if '.xyz' in str:
    counter = 0
    goodChoice = 0

    for index in range(len(str)):
        substr1 = str[index:index+4]
        if substr1 == '.xyz':
            counter += 1
  
    for index in range(len(str)):
        substr2 = str[index:index+3]
        if substr2 == 'xyz':
            goodChoice +=1
          
    if goodChoice > counter:
        return True
    else:
        return False

  elif 'xyz' in str:
    return True
  else:
    return False

str = '1.xyz.xyz2.xyz'
print(xyz_there(str))