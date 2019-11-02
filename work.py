# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:51:59 2015

@author: nitin
"""
import csv
import numpy as np
import scipy as sp
import operator
line = []
distances = []
neighbours = [] 
classVotes = {}
correct = 0
predictions = []
with open('path/iris.data','rb') as csvfile: 
    lines = csv.reader(csvfile)
    dataset = list(lines)
    print dataset
for x in range(len(dataset)-1):
    for y in range(4):
        dataset[x][y] = float(dataset[x][y])
np.random.shuffle(dataset)
train = dataset[len(dataset)*1/3:]
test = dataset[:len(dataset)*1/3]
for i in range(len(test)):
    _loc_test = test[i]
    for j in range(len(train)):
        _loc_train =train[j]
        distance = 0
        for k in range(4):
            #print _loc_test[k] - _loc_train[k]
            distance += pow((_loc_test[k] - _loc_train[k]),2)
            #print distance
        distace = np.sqrt(distance)
        distances.append((train[j],distance))
distances.sort(key = operator.itemgetter(1))
for x in range(2):
    neighbours.append(distances[x][0])
for x in range (len(neighbours)):
    response = neighbours[x][-1]
    if response in classVotes:
        classVotes[response] += 1
    else:
        classVotes[response] = 1
sortedVotes = sorted(classVotes.iteritems(), key = operator.itemgetter(1), reverse = True)
predictions.append(sortedVotes[0][0])
for x in range(len(test)):
    if test[x][-1] == predictions[x]:
        correct +=1
    print((correct/float(len(test)))*100)