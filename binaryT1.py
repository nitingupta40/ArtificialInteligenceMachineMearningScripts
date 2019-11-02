# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:52:00 2015

@author: nitin
"""

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
        
    def add(self,val):
        if(self.root ==None):
            self.root =Node(val)
        else:
            self.add(val,self.root)
    def _add(self,val,node):
        if(val<node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val,node.right)
            else:
                node.right =Node(val)
                
    def find(self,val):
        if(self.root != None):
            return self.find(val,self.root)
        else:
            return None
    
    def _find(self,val,node):
        if(val ==node.value):
            return node
        elif(val < node.value and node.left !=None):
            self._find(val, node.left)
        elif(val> node.value and node.right!= None):
            self._find(val, node.right)
        
    def deleteTree(self):
        self.root = None
        
    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)


    def _printTree(self,node):
        if(node != None):
            self._printTree(node.left)
            print str(node.value) +''
            self._printTree(node.right)

tree = Tree()
tree.add(3)
tree.add(2)
tree.add(9)
tree.add(1)
tree.add(8)

#tree.printTree()
print (tree.find(3)).value
print tree.find(10)
tree.deleteTree()
tree.printTree()
        
            
            