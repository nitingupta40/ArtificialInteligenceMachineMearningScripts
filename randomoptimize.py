# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:34:42 2015

@author: nitin
"""

import optimization

def randomoptimize(domain, costf):
    best = 999999999
    bestr = None
    for i in range(1000):
        r =[random.randint(domain[i][0], domain[i][1])
        for i in range(len(domain))]
        if cost<best:
            best = cost
            bestr = r
        return r
    
 