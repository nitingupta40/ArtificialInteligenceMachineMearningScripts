# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 13:37:17 2015

@author: nitin
"""
import math
def euclideanDistance(x,y):
    return math.sqrt(sum([(a-b)**2 for (a,b) in zip(x,y)]))
    

