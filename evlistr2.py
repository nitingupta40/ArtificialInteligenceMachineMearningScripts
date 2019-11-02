# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 04:04:14 2015

@author: nitin
"""
import random
import string
import numpy as np
source ="djawlkdjwqlkd"
target = "Hello, world!"
GENSIZE = 20
genepool = []
def calc_fitness(source, target):
    fitness =0
    for i in range(0,len(source)):
        fitness += np.square(ord(target[i]) - ord(source[i]))
    return fitness
for i in range(0, GENSIZE):
    dna = [random.choice(string.printable[:-5]) for j in range(0 , len (target))]
    fitness = calc_fitness(dna,target)
    candidate = {'dna':dna, 'fitness': fitness }
    genepool.append(candidate)

def random_parent(genepool):
    wRndNr = random.random()* random.random()*(GENSIZE-1)
    wRndNr = int(wRndNr)
    return (genepool[wRndNr])

def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]
    start = random.randint(0,len(parent2['dna'])-1)
    stop = random.randint(0, len(parent2['dna'])-1)
    if start >stop:
        stop,start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]
    charpos = random.randint(0,len(child_dna)-1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1,1))
    child_fitness = calc_fitness(child_dna, target)
    return({'dna': child_dna, 'fitness':child_fitness})
    
while True:
    genepool.sort(key = lambda candidate: candidate['fitness'])
    if genepool[0]['fitness'] ==0:
        break
    parent1 = random_parent(genepool)
    parent2 = random_parent(genepool)
    
    child = mutate(parent1, parent2)
    if child['fitness'] < genepool[-1]['fitness']:
        genepool[-1] = child
        
