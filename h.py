# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:54:54 2015

@author: nitin
"""

class solution:
        s =['a']    
        res = 0
        for i in s:
            print(int(i ,1))
            res = 26*res + int(i ,36) -9
           