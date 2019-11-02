# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 13:50:13 2015

@author: nitin
"""
import numpy as np
def sigmoid(z):
    return 1.0/(1.0 +np.exp(-z))
sigmoid_vec = np.vectorize(sigmoid)
def feedforward(self,a):
    for b, w in zip(self.biases, self.weights):
        a = sigmoid_vec(np.dot(w,a)+b)
    return a