# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:49:12 2015

@author: nitin
"""
# this code is written in python
# this function will execute only once
def _fn_oneitetarion(_count):
    _count = _count +1
    _itr = 1
    #print itr
    #print count
    return _count,_itr
#this is main function (in Cor C++)
#itr is a boolean
_itr = 0
_count =0
while _itr==0:
    _a,_itr = _fn_oneitetarion(_count)
    print _a,_itr
    

    