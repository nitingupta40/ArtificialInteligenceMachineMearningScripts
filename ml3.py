# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:06:32 2015

@author: nitin
"""






t = 2 * np.pi / 3 pl.plot([t, t], [0, np.cos(t)], color=’blue’, linewidth=2.5, linestyle="--") pl.scatter([t, ], [np.cos(t), ], 50, color=’blue’)
pl.annotate(r’$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$’, xy=(t, np.sin(t)), xycoords=’data’, xytext=(+10, +30), textcoords=’offsetpoints’, fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
pl.plot([t, t],[0, np.sin(t)], color=’red’, linewidth=2.5, linestyle="--") pl.scatter([t, ],[np.sin(t), ], 50, color=’red’)
pl.annotate(r’$cos(\frac{2\pi}{3})=-\frac{1}{2}$’, xy=(t, np.cos(t)), xycoords=’data’, xytext=(-90, -50), textcoords=’offsetpoints’, fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) 

