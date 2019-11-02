# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:15:09 2015

@author: nitin
"""
import numpy as np
from scipy import fftpack

time_step = 0.02
period =5
time_vec = np.arange(0,20, time_step)
sig = np.sin(2* np.pi /period * time_vec ) +.5* np.random.randn(time_vec.size)

sample_freq = fftpack.fftfreq(sig.size, d= time_step)
sig_fft = fftpack.fft(sig)
print(sig_fft)