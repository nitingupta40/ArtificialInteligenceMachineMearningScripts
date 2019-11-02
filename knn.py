# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 15:45:15 2015

@author: nitin
"""
import numpy as np
import scipy.spatial.distance as ssd
import time

def read_data(fn):
    #read dataset and separate into input data and label data
    # read dataset file
    with open(fn) as f:
        raw_data = np.loadtxt(f, delimiter = ',', dtype ="float", skiprows =1, usecols=None)
    #initialize list
    data = []
    label = []
    #assign input dtaa and label data
    for row in raw_data:    
        data.append(row[:-1])
        label.append(int(row[:-1]))
    #return input data and lable data
        return np.array(data, np.array(label))
        
def knn(k, dtrain, dtest, dtr_label, dist=1):
    """k-nearest neighbours"""
    #initialize list to store predicted class
    pred_class = []
    #for each instance in data testing
    #calculate distance in respect to data training
    for ii, di in enumerate(dtest):
        distence = [] # initialize list to store distaace
        