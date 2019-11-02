# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:20:16 2015

@author: nitin
"""
from array import *
firstarray = array('c',)
middlearray = array('c',)
lastarray = array('c',)
finalstring = array('c',)
class solution:
    text ="PAYPALISHIRING"
    for i in range(len(text)):
        if(i%4 == 0):
            firstarray.append(text[i])
        if(i%4 == 2):
            lastarray.append(text[i])
        if((i%4==1) or (i%4==3)):
            middlearray.append(text[i])
    print("1",firstarray)
    print("2",middlearray)
    print("3",lastarray)
    finalstring =firstarray+middlearray+lastarray
    print (finalstring)
    row = 3
    