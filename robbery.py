# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:25:10 2015

@author: nitin
"""

from array import *
class solution:
    num = array('c',('w','e','e','c'))
        
    max_3_house_before, max_2_house_before, adjacent =0,0,0
    for cur in num:
        max_3_house_before, max_2_house_before, adjacent  =\
        max_2_house_before,adjacent,max(max_3_house_before+cur,max_2_house_before+cur)
       print(max_3_house_before)
   