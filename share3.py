# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:10:55 2015

@author: nitin
"""

class solution:
    
    prices = [2323,11,11,233,333]
    k =4
    if k >= len(prices)//2:
        print( sum(i -j for i,j in zip(prices[1:],prices[:-1])  if i-j >0))
    hold, release = [float('-inf')]*(k+1),[0]*(k+1)
    for p in prices:
        for i in range(1,k+1):
            release[i] = max(release[i],hold[i]+p)
            hold[i] = max(hold[i],release[i-1]-p)
    print(release[k])