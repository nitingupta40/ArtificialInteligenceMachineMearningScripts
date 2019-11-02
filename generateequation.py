# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 17:44:06 2015

@author: nitin
"""

import random
from operator import itemgetter
import operator

def _fn_generateEquation(n):
    num = []
    eqn =[]
    constant =[]
    operator =[]
    for i in range(n):
        k = random.randint(1,n)
        num.append(k)
        #num.get()
   #print num
    for i in range (len(num)):
        k = random.randint(1,399)
        constant.append(k)
   #print constant
#    for i in range(len(num)):
#        eqn.append(num[i],constant[i])
#        print {num[i]:constant[i]}
#    print eqn
    for i in range (len(num)-1):
        k = random.randint(0,1)
        if k == 0:
            operator.append('+')
        else:
            operator.append('-')
    for i in range (len(num)-1):
        eqn.append((constant[i],num[i],operator[i]))
    
    print eqn     
    
    #print sorted(eqn.items(),key = itemgetter(1))
       
    


        
_fn_generateEquation(3)