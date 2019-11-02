# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:49:40 2015

@author: nitin
"""
import pylab as pi 
import numpy as np
pi.figure(figsize = (8,6), dpi =80)
pi.subplot(1,1,1)
X = np.linspace(-np.pi, np.pi, 256, endpoint =True)
C,S = np.cos(X), np.sin(X)
pi.plot(X,C, color = "blue", linewidth = 4.0, linestyle ="-", label = "cosine")
pi.plot(X,S, color = "green", linewidth = 1.0, linestyle = "-", label = "sine" )
pi.xlim(X.min() *1.1, X.max() *1.1)
pi.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi]) 
pi.ylim(C.min()*1.1,C.max()*1.1)

pi.yticks([-1, 0, +1])
ax = pi.gca()
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('yellow')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
pi.legend(loc = 'upper center')

t = 2* np.pi/3
pi.plot([t,t],[0,np.cos(t)], color = 'blue' , linewidth =2.5, linestyle ="--")
pi.scatter([t,],[np.cos(t), ],50,color ='blue')

pi.annotate(r’$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$’, xy=(t, np.sin(t)), xycoords=’data’, 
xytext=(+10, +30), textcoords=’offsetpoints’, fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
pi.plot([t, t],[0, np.sin(t)], color=’red’, linewidth=2.5, linestyle="--") 
pi.scatter([t, ],[np.sin(t), ], 50, color=’red’)
pi.annotate(r’$cos(\frac{2\pi}{3})=-\frac{1}{2}$’, xy=(t, np.cos(t)), xycoords=’data’, xytext=(-90, -50), textcoords=’offsetpoints’, fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) 


pi.show()