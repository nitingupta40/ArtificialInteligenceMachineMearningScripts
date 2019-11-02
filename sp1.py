# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:43:03 2015

@author: nitin
"""
import numpy as np
from scipy import stats
from scipy import io as spio
a=  np.ones((3,3))
spio.savemat('file.mat', {'a':a})
data = spio.loadmat('file.mat',struct_as_record =True) 
print(data['a'])