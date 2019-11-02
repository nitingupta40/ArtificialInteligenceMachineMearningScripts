# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:42:26 2015

@author: nitin
"""
from array import *
class solution:
    arr =array('i',[12,1,3,32,43,54,65,65,65])
    print(len(arr)/2)
    a = sorted(arr)[len(arr)/2]
    print(a)