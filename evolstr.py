# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 03:40:09 2015

@author: nitin
"""
import numpy as np
import random
source ="djawlkdjwqlkd"
target = "Hello, world!"

def fitness(source, traget):
    fitval = 0
    for i in range(0, len(source)):
        fitval += np.square(ord(target[i]) - ord(source[i]))
    return (fitval)
    
def mutate(source):
    charpos = random.randint(0, len(source)-1)
    parts = list(source)
    parts[charpos] = chr(ord(parts[charpos]) + random.randint(-1,1))
    return (''.join(parts))

fitval = fitness(source, target)
i = 0
while True:
    i +=1
    m = mutate(source)
    fitval_m = fitness(m,target)
    if fitval_m <fitval:
        fitval = fitval_m
        source = m
        print "%5i %15i %14s" %(i,fitval_m,m)
    if fitval ==0:
        break
    