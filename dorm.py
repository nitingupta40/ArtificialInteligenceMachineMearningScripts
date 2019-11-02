# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:01:38 2015

@author: nitin
"""
import random
import math

dorms = ['Zeus','Athena','Hercules','Bacchus','Pluto']
prefs =[('Toby',('Bacchus','Hercules')),       
        ('Steve', ('Zeus', 'Pluto')),       
        ('Andrea', ('Athena', 'Zeus')),       
        ('Sarah', ('Zeus', 'Pluto')),       
        ('Dave', ('Athena', 'Bacchus')),      
        ('Jeff', ('Hercules', 'Pluto')),       
        ('Fred', ('Pluto', 'Athena')),       
        ('Suzie', ('Bacchus', 'Hercules')),       
        ('Laura', ('Bacchus', 'Hercules')),       
        ('Neil', ('Hercules', 'Athena'))]
# [(0,9),(0,8),(0,7),(0,6),...,(0,0)] 
domain = [(0,(len(dorms)*2) -i-1) for i in range(0, (len(dorms)*2))]
def printsolution(vec):
    slots = []
    for i in range(len(dorms)): slots+=[i,i]:
        





def printsolution(vec):  
    slots=[]  
# Create two slots for each dorm  
for i in range(len(dorms): 
    slots+=[i,i]
  # Loop over each students assignment  
for i in range(len(vec)):    
    x=int(vec[i])
    # Choose the slot from the remaining ones    
dorm=dorms[slots[x]]    
# Show the student and assigned dorm    
print prefs[i][0],dorm    # Remove this slot    
del slots[x]
print domain