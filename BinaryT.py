# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:32:44 2015

@author: nitin
"""
class BinaryTree():
    def __init__(self,rootid):
        self.left = None
        self.right = None
        self.rootid = rootid
        
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    
    def insertRight(self,newNode):
        if self.right ==None:
            self.right=BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
            
    def insertLeft(self,newNode):
        if self.left ==None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left
def printTree(tree):
    if tree!=None:
        print(tree.getleftchild())
        print(tree.getNodeValue())
        printTree(tree.getrightchild())
def testTree():
    mytree = BinaryTree("this")
    mytree.insertLeft("is")
    mytree.insertRight("me")
    mytree.insertLeft("hi")
    printTree(mytree)
            
        
