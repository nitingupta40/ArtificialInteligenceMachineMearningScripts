# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:33:58 2015

@author: nitin
"""

class solution:
    x = 123
    rev_num =0
    count =len(str(123))
    for i in range (len(str(123))):
        print("hey")
        if (x != 0 & x >0):
            num = x%10
            print(x)
            rev_num = rev_num + num*pow(10,count-(i+1))
            x /= 10
            
                            
            print(rev_num)
            print(i)