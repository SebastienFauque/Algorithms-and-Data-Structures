# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 09:25:57 2021

@author: Sebastien
@fileName:Starbucks_max_profit.py
@project:
    
    This question was asked by: Starbucks

1. Given a list of stock prices in ascending order by datetime, write a function that outputs the max profit by buying and selling at a specific interval.

Example:

stock_prices = [10,5,20,32,25,12]

get_max_profit(stock_prices) -> 27
"""

def get_max_profit(stock_prices):
    mini = min(stock_prices)
    maxi = max(stock_prices)
    return maxi-mini

stock_prices = [10,5,20,40,25,12]

print(get_max_profit(stock_prices))