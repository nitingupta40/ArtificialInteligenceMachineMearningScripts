# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 13:30:36 2015

@author: nitin
"""

import random

def gausscluster(center, stdDev, count = 50):
    return [(random.gauss(center[0],stdDev), random.guass(center[1], stdDev)) for _ in range(count)]
def makeDummyData():
    return gausscluster((-4,0), 1) + gausscluster((4,0), 1)