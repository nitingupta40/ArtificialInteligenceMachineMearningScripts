# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:55:19 2015

@author: nitin
"""
import numpy as np

is_prime = np.ones((100,), dtype = bool)
is_prime[0:2] = 0
N_max = int(np.sqrt(len(is_prime)))
print(N_max)
a = np.random.random_integers(0,10,15)
print(a)
for j in range (2, N_max):
        
    is_prime[2*j ::j] = False
 
    