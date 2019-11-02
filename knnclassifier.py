# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 13:40:32 2015

@author: nitin
"""

import heapq

def makeKNNClassifier(data, labels, k, distance):
    def classify(x):
        closestPoints = heapq.nsmallest(k, enumerate(data),
                                       key = lambda y: distance(x ,y[1]))
        closestLabels = [labels[i] for (i, pt) in closestPoints]
        return max(set(closestLabels), key=closestLaabels.count)
    return classify