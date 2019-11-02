# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:40:49 2015

@author: nitin
"""

class solution:
    text ="abcdeafa"
    start = maxlength =0
    usedchar = {}
    
    for i in range(len(text)):
        if text[i] in usedchar and  start <= usedchar[text[i]]:
            start = usedchar[text[i]] +1
        else:
            maxlength = max(maxlength, i- start+1)
            
        usedchar[text[i]] =i
        print( maxlength)