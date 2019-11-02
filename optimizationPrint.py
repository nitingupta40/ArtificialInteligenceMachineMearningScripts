# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:58:03 2015

@author: nitin
"""
import optimization
s =[0,1]
for d in range(len(s)/2):
    name = people[d][0]
    origin = people[d][1]
    out = flights[(origin,destination)][s[d]]
    ret = flights[(destination, origin)][s[d+1]]
    print '%10s10s% %5s-%5s %3s %5s-%5s $%3s' %(name, origin,out[0],out[1],out[2],ret[0], ret[1],ret[2])

print ret


