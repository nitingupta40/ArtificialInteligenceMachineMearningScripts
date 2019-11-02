# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 02:22:24 2015

@author: nitin
"""
from array import *
class solution:
    sam_array = array('i',[1,2,3,2,7,3,8,4])
    
    for i in range(len(sam_array)-1):
        if(sam_array[i] > sam_array[i+1]):
           temp = sam_array[i+1]
           sam_array[i+1] = sam_array[i]
           sam_array[i] = temp
        print(i, ":elements of array",sam_array[i])
        
