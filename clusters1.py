# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:37:05 2015

@author: nitin
"""
from PIL import Image,ImageDraw
import random
import math

def pearson(v1,v2):  
    sum1=sum(v1)  
    sum2=sum(v2)
    sum1Sq=sum([pow(v,2) for v in v1])  
    sum2Sq=sum([pow(v,2) for v in v2])
    pSum=sum([v1[i]*v2[i] for i in range(len(v1))])
    num=pSum-(sum1*sum2/len(v1))  
    den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))  
    if den==0: return 0
    return 1.0-num/den    
    
def scaledown(data, distance = pearson, rate =0.01):
    n = len(data)
    realdist= [[distance(data[i], data[j]) for j in range(n)] for i in range(0,n)]
    outersum = 0.0
    loc = [[random.random(), random.random()] for i in range(n)]
    fakedist = [[0.0 for i in range(n)] for i in range(n)]
    lasterror = None
    for m in range(0,1000):
        for i in range(n):
            for j in range(n):
                fakedist[i][j] =math.sqrt(sum([pow(loc[i][x] - loc[j][x],2) for x in range(len(loc[i]))]))
    grad = [[0.0,0.0] for i in range(n)]
    totalerror =0
    for k in range(n):
        for j in range(n):
            if j==k: continue
            errorterm =(fakedist[j][k] - realdist[j][k])/ realdist[j][k]
            grad[k][0] += ((loc[k][0] - loc[j][0]) /fakedist[j][k]) * errorterm
            grad[k][1] += ((loc[k][1] - loc[j][0]) /fakedist[j][k]) * errorterm 
            totalerror + abs(errorterm)
    print totalerror
    if lasterror and lasterror<totalerror: exit
    lasterror = totalerror
    for k in range (n):
        loc[k][0] -= rate *grad[k][0]
        loc[k][1] -= rate *grad[k][1]
    return loc
 
def draw2d(data, labels, jpeg ='mdsd.jpg'):
    img = Image.new('RGB', (2000,2000),(255,255,255))
    draw = ImageDraw.Draw(img)
    for i in range(len(data)):
        x = (data[i][0] + 0.5)*1000
        y = (data[i][1] + 0.5)*1000
        draw.text((x,y), labels[i],(0,0,0))
    img.save(jpeg,'JPEG')   

