# -*- coding: utf-8 -*-5
"""
Created on Thu Apr 23 16:29:45 2015

@author: nitin
"""
import pylab as pi
import numpy as np
x = np.linspace(-np.pi, np.pi, 256, endpoint =True)
c,s =  np.tanh(x), np.tan(x)
pi.plot(x,c)
pi.plot(x,s)
pi.show()