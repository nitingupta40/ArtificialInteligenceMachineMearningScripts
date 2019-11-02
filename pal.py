# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:43:40 2015

@author: nitin
"""

class solution:
    name = "nitinwwwer"
    data = {}
    print(name[::-1])
    lenstr = len(name) 
    while (lenstr!= 0):
        lenstr -= 1
        for i in range(lenstr):
            print(name[lenstr::-1])
            data.fromkeys(name[lenstr::-1],i) 
            print (data)
           