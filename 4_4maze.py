# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:27:05 2015

@author: nitin
"""
import random
import numpy as np
class fourfourmaze:
    _dimention_maze = np.array([[1,0,0],[0,0,0],[0,0,0]])
    _openloc =_dimention_maze[0][0]
    _iter = 1000
    _current_loc = np.array([[0],[0]])
    print _current_loc 
    print _openloc
    _row = 3
    _col = 3
    move = random.randrange(4)
    if move ==0:
        print _dimention_maze[_row-1][_col] 
        print 'left' 
    if move ==1:
        print 'right'
    if move ==2:
        print 'top'
    if move == 3:
        print 'bottom'
   # for row in range(_row):
#    if(_current_loc >_dimention_maze[0][2] and current_loc < _dimention_maze[2][2] and
#        _current_loc > _dimention_maze[2][0] and current_loc < _dimention_maze [2][2]):
#            
#  
        
    