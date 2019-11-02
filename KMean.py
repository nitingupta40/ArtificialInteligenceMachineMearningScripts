# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:26:38 2015

@author: nitin
"""
import random
import numpy as np
import math as mp
import csv
import operator
randompoints =[]
min_point =[]
clusters=[]
centroid =[]
def KMean(_fileName, _numOfClusters):
    with open(_fileName,'rb')as _file:
        _line = csv.reader(_file)
        #np.random.shuffle(_line)
        _dataset = list(_line)
    for x in range (len(_dataset)-1):
        for y in range(4):
            _dataset[x][y] = float (_dataset[x][y])   
    for _num in range(_numOfClusters):
        _rand = random.randrange(0,len(_dataset))
        randompoints.append(_dataset[_rand])
    if (len (centroid)==0):
        for i in range(len(randompoints)):
            centroid.append(randompoints[i])
            #print len(centroid)
    for i in range (1000):            
        for points in (range(len(_dataset)-1)):    
            for rand in centroid:
                for i in range (4):
                    dif =+ pow((rand [i]-_dataset[points][i]),2)            
                    dif = np.sqrt(dif)
                min_point.append((rand,dif))
            min_point.sort(key = operator.itemgetter(1))
            clusters.append((min_point[0],_dataset[points]))
            del min_point[:]
        for _loc_centroid in range (len(centroid)-1):
            for _loc_clusters in range (len(clusters)-1):
                 if centroid[_loc_centroid] == clusters[_loc_clusters][0][0]:
                      centroid[_loc_centroid][:-1] = (np.array( centroid[_loc_centroid][:-1]) +np.array(clusters[_loc_clusters][1][:-1]))/2
    print centroid
_path='path/iris.data'
_numOfClusters = 3
KMean(_path,_numOfClusters)
    
