# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:24:03 2015

@author: nitin
"""

def _add(node,v):
    new = [v,[],[]]
    if node:
        left,right =node[1:]
        if not left:
           left.extend(new)
        elif not right:
            right.extend(new)
        else:
            _add(left,v)
    else:
        node.extend(new)

def binary_tree(s):
    root=[]
    for e in s:
        _add(root,e)
    return root

def traverse(n, order):
    if n:
        v = n[0]
        if order =='pre':
            yield v
        for left in traverse(n[1], order):
            yield left
        if order =='in':
            yield v
        for right in traverse(n[2], order):
            yield right
        if order == 'post':
            yield v

t =binary_tree('A B c d e f'.split())
print t