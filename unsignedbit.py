# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:58:16 2015

@author: nitin
"""

class solution:
    i = 3233333
    x =(bin(i)[:1:-1]).ljust(32,'0')
    print(str(x).count('1'))
    print( int(x,base =2))