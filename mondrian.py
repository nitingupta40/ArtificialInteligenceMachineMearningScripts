# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:59:07 2015

@author: nitin
"""

import random
from Tkinter import *
from copy import deepcopy
import math
def _fn_canvas():
    master = Tk()
    _canvas_width = 360
    _canvas_height = 360
    canvas = Canvas(master, width = _canvas_width, height =_canvas_height) 
    return canvas

def _point(self,x,y):
    self.x = x
    self.y = y

def _fn_Coordinates():
    _point.x = random.randint(0,360)
    _point.y = random.randint(0,360)
    return _point.x,_point.y
    
def _fn_lineCoordinates():
    _linepoints =[]
    for i in range (5):
        _point.x, _point.y = _fn_Coordinates()
        _linepoints.append((_point.x,_point.y))
    return _linepoints

def _fn_alllineCordinates():
    _alllinepoints =[]
    _linepoints = _fn_lineCoordinates()
    _alllinepoints =deepcopy(_linepoints)
#    for i in range(len(_linepoints)-1):
#        _alllinepoints.append((_linepoints[i][0],_linepoints[i+1][1]))
#        _alllinepoints.append((_linepoints[i+1][0], _linepoints[i][1]))
    return _alllinepoints
       
def _fn_color():
    _color = ['red', 'yellow', 'blue']
    itr = random.randint(0,2)
    return _color[itr]
 
def _fn_ractangel(_linepoints):
    _ractangle = set()
    _ractColor =[]
    __linepoints = _linepoints
    for i in range(len(__linepoints)-1):
        _ractangle.add((__linepoints[i], __linepoints[i+1]))
        __color = _fn_color()
        _ractColor.append(__color)
    return _ractangle,__linepoints,_ractColor
    
def _fn_minwidthheightrectangle(_linepoints):
    _linepoints = _linepoints
    _ractangle,_linepoints,_rectColor = _fn_ractangel(_linepoints)
    print _ractangle
    __ractangle =[]
    __nwractangle =[]
    _rejected =[]
    _numract = len(_ractangle)
    #print _ractangle
    for i in range (len(_ractangle)):
        __ractangle.append (_ractangle.pop())
    for i in range(len(__ractangle)):
        if ((abs(__ractangle[i][0][0] - __ractangle[i][1][0])>30) and (abs(__ractangle[i][0][1] - __ractangle[i][1][1])) >30):
             __nwractangle.append(__ractangle[i])
        else:
             _rejected.append(__ractangle[i])
    _numrejected = len(_rejected)
    ratio = (float(_numrejected)/(_numract))
    print(ratio)
    print __nwractangle,_linepoints,_rectColor,"yes"
    
    return __nwractangle,_linepoints,_rectColor,ratio

def _fn_genetics():
    
    _linepoints = _fn_alllineCordinates()
    _newgenerationpoints =[]
    
    _newpopulation =[]
    _ractangle,_linepoints,_rectColor,ratio = _fn_minwidthheightrectangle(_linepoints)
    if (ratio >= 0.33):
        _newgenerationpoints = _fn_lineCoordinates()
        _numrandom = random.randint(1, (len(_linepoints)-1))
        _nindex = random.randint(0,1)
        if (_nindex ==0):
            for i in range (_numrandom):
                _newpopulation.append (_newgenerationpoints[i])
            for i in range(_numrandom, len(_linepoints)):
                _newpopulation.append( _linepoints[i])
        else:
            for i in range (_numrandom):
                _newpopulation.append (_linepoints[i])
            for i in range(_numrandom, len(_linepoints)):
                _newpopulation.append( _newgenerationpoints[i])
        _ractangle,_linepoints,_rectColor,ratio = _fn_minwidthheightrectangle(_newpopulation)            
    
    print "genetic input"
    return _ractangle,_newpopulation,_rectColor

    
def _fn_removeoverlappingRactangle():
    _nwractangle,_linepoints,_rectColor = _fn_genetics()
    _isoverlapping = False
    _nooverlappingractangle = set()
    _nooverlapping = []
    _nooverlapping.append(_nwractangle[0])
    for i in range (len(_nwractangle)):
        for j in range(len(_nooverlapping)):
            if(((_nwractangle[i][1][1] <= _nooverlapping[j][0][1])and(_nwractangle[i][0][1] >= _nooverlapping[j][1][1])
                and(_nwractangle[i][1][0] <= _nooverlapping[j][0][0])and(_nwractangle[i][0][0] >= _nooverlapping[j][1][0]))):
                    if _nwractangle[i] not in _nooverlapping:                     
                        _nooverlapping.append(_nwractangle[i]) 
                        _nooverlappingractangle.add(_nwractangle[i])
            
                    else: 
                        continue
            else:
                continue
#    print _nooverlappingractangle
#    print _nooverlapping
    return _nooverlapping,_linepoints,_rectColor
    #return _nooverlappingractangle           

def _fn_rightangle():
    print "hi"
   
def _fn_drawRactangle():
    _ractCoordinades,_lineCoordinates,_ractColor = _fn_removeoverlappingRactangle()
    canvas = _fn_canvas()
    canvas.pack()
    for  i in range (len(_lineCoordinates)-1):
        canvas.create_oval(_lineCoordinates[i][0]-3,_lineCoordinates[i][1]-3,_lineCoordinates[i][0]+3,_lineCoordinates[i][1]+3,outline="Blue", fill ="Red", width=2)
    for i in range(len(_lineCoordinates)-1):
        canvas.create_line(_lineCoordinates[i][0],_lineCoordinates[i][1],0, _lineCoordinates[i][1],width=1)
        canvas.create_line(_lineCoordinates[i][0],_lineCoordinates[i][1],360,_lineCoordinates[i][1], width =1)
        canvas.create_line(_lineCoordinates[i][0],_lineCoordinates[i][1],_lineCoordinates[i][0],0,width=1)
        canvas.create_line(_lineCoordinates[i][0],_lineCoordinates[i][1],_lineCoordinates[i][0],360, width = 1)        
    for i in range(len(_ractCoordinades)):
        canvas.create_rectangle(_ractCoordinades.pop(),fill =_ractColor[i],width=6)
    canvas.create_rectangle(0,0,360,360,width =10)
    
    mainloop()
#_fn_removeoverlappingRactangle()
_fn_drawRactangle()