# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:19:50 2015

@author: nitin
"""
class solution:
    m = 5
    n = 8
    if m==n:
        print m
    mm = bin(m)[2::]
    nn = bin(n)[2::]
    if len(nn) >len(mm):
        return 0
    cur = 0
    for cc in mm:
        if cc  != nn[cur]:
            break
        cur =cur+1
        return int(mm[0:cur:] + '0' .zfill(len(mm)-cur),2)
