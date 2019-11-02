# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:49:52 2015

@author: nitin
"""
from array import *
class solution:
    a = array('i',(32,2,12,43,54,111))
    #print(sorted(a))
    tel = {'first': 1,'Second': 2}
    tel['third'] = 3
    #print ('third' in tel)
    s = set (('a','b','c','a','23'))
    #print(s.difference(('a','23')))
    volels =  'aeiou'
    check ='penasonic'
    for i in check:
        if i in volels:
            print(i)
    message ="this is me ?"
    #print(message.split())
    for words in message.split():
        print(words)
        
    wordss = ('first', 'second', 'third')
    for index, items in enumerate (wordss):
        print(index,items)
    #print (s)
    items = {'a':1, 'b':1.2, 'c':3.4}
    for key, item in items.iteritems():
       print('items', (key,item ))
    def test(name):
        return name
    this = 'nitin'
    name =test(this)
    print(name)
    