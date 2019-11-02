# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 13:34:04 2015

@author: nitin
"""
import knn
import random

def colomn(A, j):
    return [row[j] for row in A]
    
def test(data, k):
    random.shuffle(data)
    pts,lables = column(data, 0), column(data,1)
    
    trainingData = pts[:800]
    trainingLables = lables[:800]
    testData = pts[800:]
    testLables = lables[800:]
    
    f = knn.makeKNNClassifier(trainingData, trainingLables,k,knn.euclideanDistance)
    correct = 0
    total = len(testLables)
    
    for (point, label) in zip (testData, testLables):
        if f(point) == label:
            correct +=1
        accuracy = float(correct) /total     
        print accuracy
        
test()
    
    