# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:18:46 2015

@author: nitin
"""

import time
import random
import math
import xml.dom.minidom
people = [('Seymour', 'BOS'),
          ('Franny', 'DAL'),
          ('Zooey', 'CAK'),
          ('Walt','MIA'),
          ('Buddy', 'ORD'),
          ('Les', 'OMA')]

destination = 'LGA'
flights ={}
for line in file('C:\\Users\\nitin\\Desktop\\schedule.txt'):
    origin,dest,depart,arrive,price = line.strip().split(',')
    flights.setdefault((origin,dest),[])
    flights[(origin,dest)].append((depart,arrive,int(price)))

def getminutes(t):
    x = time.strptime(t, '%H:%M')
    return x[3]*60 + x[4]    

def printschedule(r):
    for d in range(len(r)/2):
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin,destination)][r[d]]
        ret = flights[(destination, origin)][r[d+1]]
        print '%10s10s% %5s-%5s %3s %5s-%5s $%3s' %(name, origin,out[0],out[1],out[2],ret[0], ret[1],ret[2])

def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
    earliestdep = 24*60
    for d in range(len(sol)/2):
        origin = people[d][1]
        outbound = flights[(origin,destination)][int(sol[d])]
        returnf = flights[(destination,origin)][int(sol[d+1])]
        totalprice += outbound[2]
        totalprice += returnf[2]
        if latestarrival < getminutes(outbound[1]): latestarrival = getminutes(outbound[1])
        if earliestdep>getminutes(returnf[0]): earliestdep = getminutes(returnf[0])
    totalwait = 0
    for d in range(len(sol)/2):
        origin = people[d][1]
        outbound = flights[(origin, destination)][int (sol[d])]
        returnf = flights[(destination, origin)][int (sol[d+1])]
        totalwait+= latestarrival - getminutes(outbound[1])
        totalwait+= getminutes(returnf[0]) - earliestdep
        if latestarrival > earliestdep: totalprice+=50
    return totalprice+totalwait

def hillclimb(domain, costf):
    sol = [random.randint(domain[i][0], domain[i][0])
    for i in range(len(domain))]
    while 1:
        neighbors = []
        for j in range(len(domain)):
            if  sol[j] > domain[j][0]:
                neighbors.append(sol[0:j] + [sol[j]+1] + sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j]-1] + sol[j+1:])
    current = costf(sol)
    best = current
    for j in range(len(neighbors)):
        cost = costf(neighbors[j])
        if cost<best:
            best = cost
            sol = neighbors[j]
    return sol
                 

def annealingoptimize(domain, costf, T= 10000.0, cool =0.95, step=1):
    vec = [float(random.randint(domain[i][0], domain[i][1])) for i in range(len(domain))]
    while T> 0.1:
        i = random.randint(0, len(domain)-1)
        dir = random.randint(-step,step)
        vecb = vec[:]
        vecb[i]+=dir
        if vecb[i]< domain[i][0]: vecb[i] = domain[i][0]
        elif vecb[i]>domain[i][1]: vecb[i] = domain[i][0] 
        ea = costf(vec)
        eb = costf(vecb)
        p = pow(math.e, (-eb -ea)/T)
        if (eb<ea or random.random() <p):
            vec = vecb
        T = T* cool
    return vec
