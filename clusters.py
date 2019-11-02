# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:58:16 2015

@author: nitin
"""
from PIL import Image, ImageDraw
from math import sqrt
def readfile(filename):
    lines =[line for line in file(filename)]
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        rownames.append(p[0])
        data.append([float(x) for x in p[1:]])
    return rownames,colnames,data
def pearson(v1,v2):
    sum1 = sum(v1)
    sum2 = sum(v2)
    sum1Sq = sum([pow(v,2) for v in v1])
    sum2Sq = sum([pow(v,2) for v in v2])
    pSum = sum([v1[i]*v2[i] for i in range (len(v1))]) 
    num = pSum -(sum1*sum2/len(v1))
    den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))  
    if den==0: return 0
    return 1.0-num/den 
        
class bicluster:  
    def __init__(self, vec, left = None, right = None, distance = 0.0,id = None):    
        self.left = left
        self.right = right
        self.vec = vec
        self.id =id
        self.distance = distance

    def hclucter(rows, distance = pearson):
        distance ={}
        currentclustid = -1
        clust = [bicluster(rows[i], id = i) for i in range (len(rows))]
        while len(clust)>1:
            lowestpair =(0,1)
            closest = distance(clust[0].vec, clust[1].vec)
            for i in range(len(clust)):
                for j in range(i+1, len(clust)):
                    if (clust[i].id, clust[j].id) not in distance:
                        distance[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)
                        d = distance[(clust[i].id,clust[j.id])]
                    if d<closest:
                        closest =d
                        lowestpair =(i,j)
        #mergevec=[(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i]])/2.0 for i in range(len(clust[0].vec))]
        mergevec=[(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in range(len(clust[0].vec))]
        newcluster = bicluster(mergevec, left = clust[lowestpair[0]], right = clust[lowestpair[1]], distance = closest, id = currentclustid)
        currentclustid =-1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)        
        return clust[0]

    def printclust(clust, labels = None, n=0):
        for i in range(n):
            print ' ',
        if clust.id <0:
            print '-'
        else:
            if labels ==None: print clust.id            
            else: print labels[clust.id] 
        if clust.left !=None:
            printclust(clust.left, lables = labels, n= n+1)
        if clust.right != None:
            printclust(clust.right, lables = labels,n=n+1)

def scaledown(data, distance = pearson, rate = 0.01):
    n = len(data)
    realdist = [[distance(data[i],data[j]) for j in range(n)] for i in range(0,n)]
    outersum = 0.0
    loc = [[random.random(), random.random()] for i in range(n)]
    fakedist = [[0.0 for j in range(n)] for i in range(n)]
    lasterror = None 
    for m in range(0,1000):
        for i in range(n):
            for j in range(n):
                fakedist[i][j] = sqrt(sum([pow(loc[i][x] - loc[j][x],2)])for x in range(len(loc[i])))
    grand = [[0.0,0.0] for i in range(n)]
    totalerror =0
    for k in range(n):
        for j in range(n):
            if j==k : 
                continue
            errorterm =(fakedist[j][k] -realdist[j][k])/realdist[j][k]
            grad[k][0]+= ((loc[k][0] - loc[j][0])/fakedist[j][k])* errorterm
            grad[k][1]+= ((loc[k][1] - loc[j][1])/fakedist[j][k])* errorterm
            totalerror+=abs(errorterm)    
        print totalerror
    # If the answer got worse by moving the points, we are done    
        if lasterror and lasterror<totalerror: break    
        lasterror=totalerror
    # Move each of the points by the learning rate times the gradient    
        for k in range(n):      
            loc[k][0]-=rate*grad[k][0]      
            loc[k][1]-=rate*grad[k][1]
    return loc 
  #To view this, you can use the PIL again to generate an image with all the labels of all the different items plotted at the new coordinates of that item.
def draw2d(data,labels,jpeg='mds2d.jpg'):  
    img=Image.new('RGB',(2000,2000),(255,255,255))  
    draw=ImageDraw.Draw(img)  
    for i in range(len(data)):    
        x=(data[i][0]+0.5)*1000    
        y=(data[i][1]+0.5)*1000    
        draw.text((x,y),labels[i],(0,0,0))  
    img.save(jpeg,'JPEG')