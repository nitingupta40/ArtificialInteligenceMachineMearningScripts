# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:11:06 2015

@author: nitin
"""
import bisect
import itertools
import operator

class _BNode(object):
    __slots__ =["tree","contents","children"]
    
    def __init__(self, tree, contents=None,children=None):
        self.tree = tree
        self.contents = contents or []
        self.children = children or []
        if self.children:
            assert len(self.contents)+1 == len(self.children),\
            "one more child than data item required"
    def __repr__(self):
        name = getattr(self, "children",0) and "Branch" or "Leaf"
        return "<%s %s>" %(name, ",".join(map(str,self.contents)))
            
    def lateral(self, parent,parent_index, dest, dest_index):
        if  parent_index >dest_index:
            dest.contents.append(parent.contents[dest_index])
            parent.contents[dest_index] = self.contents.pop(0)
            if self.children:
                dest.children.append(self.contents.pop(0))
            else:
                dest.contents.insert(0,parent.contents[parent_index])
                parent.contents[parent_index] = self.contents.pop()
                if self.children:
                    dest.children.insert(0,self.children.pop())
                    
    def shrink(self,ancestors):
        parents = None
        if ancestors:
            parent,parent_index = ancestors.pop()
            if parent_index:
                left_sib = parent.children[parent_index -1]
                if len(left_sib.contects) < self.tree.order:
                    self.lateral(parent, parent_index, left_sib, parent_index-1)
                    return
                    
            if parent_index +1 < len(parent.children):
                right_sib = parent.children[parent_index +1]
                if len(right_sib.contents)<self.tree.order:
                    self.lateral(parent,parent_index, right_sib,parent_index+1)
                    return
        
        centre = len(self.contents)//2
        