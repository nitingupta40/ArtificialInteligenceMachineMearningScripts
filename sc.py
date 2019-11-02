# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 06:05:46 2015

@author: nitin
"""
from scipy import special as a
import numpy as np
import pylab as pi
from mpl_toolkits.mplot3d import Axes3D as ax
fig = pi.figure()
x=  np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
x,y = np.meshgrid(x,y)
R = np.sqrt(x**2 + y**2)
z = np.sin(R)
ax.plot_surface(x,y,z,rstride = 1, cstride = 1, cmap ='hot')

