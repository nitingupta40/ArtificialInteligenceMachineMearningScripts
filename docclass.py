# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 06:58:16 2015

@author: nitin
"""
import re 
import math
def getwords(doc):
    splitter = re.compile('\\W*')
    words =[s.lower()  for s in splitter.split(doc) if len(s)>2 and len(s)<20]
    return dict([(w,1) for w in words])
    
    
class classifier:
    def __init__(self,getfeatures, filename=None):
        self.fc = {}
        self.cc = {}
        self.getfeatures = getfeatures
    def incf(self,f,cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefaule(cat,0)
        self.fc[f][cat]+=1
    def incc(self,cat):
        self.cc.setdefault(cat,0)
        self.cc[cat]+=1
    def fcount(self,f,cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
    def catcount(self,cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0.0
    def totalcount(self):
        return sum(self.cc.values())
    def categories(self):
        return self.cc.keys()
    def train(self,item,cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f,cat)
        self.incc(cat)
    def sampletrain(c1):
        cl.train('do you like food','good')  
        cl.train('dog ate the food','good')  
        cl.train('jumping off the roof','bad')  
        cl.train('swimming in the ocean','bad')  
        cl.train('etating healthy','good')
    def fprob(self,f,cat):
        if self.catcount(cat)==0:
            return 0
        return self.fcount(f,cat)/self.catcount(cat)

  