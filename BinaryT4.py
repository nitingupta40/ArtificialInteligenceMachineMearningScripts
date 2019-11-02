# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 03:42:34 2015

@author: nitin
"""

class TreeNode:
    def __init__(self, key,val,left=None,right=None,parent=None):
        self.key =key
        self.payload =val
        self.leftchild =left
        self.rightchild =right
        self.parent =parent
    
    def hasleftChild(self):
        return self.hasleftChild
    
    def hasrightChild(self):
        return self.hasrightChild
    
    def isleftChild(self):
        return self.parent and self.parent.leftchild ==self
        
    def isrightChild(self):
        return self.parent and self.parent.rightchild ==self
        
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.leftchild or self.rightchild)
    
    def hasanyChildren(self):
        return self.leftchild or self.rightChild
        
    def hasbothChildren(self):
        return self.leftchild and self.rightchild
        
    def replacenodeData(self, key, value, l_child, r_child):
        self.key = key
        self.payload = value
        self.isleftChild = l_child
        self.isrightChild = r_child
        if self.hasleftChild():
            self.leftchild.parent = self
        if self.hasrightChild():
            self.rightchild.parent = self
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size =0
        
    def length(self):
        return self.size
        
    def __len__(self):
        return self.size
        
    def put(self, key, val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1
            
    def _put(self, key,val,currentNode):
        if key < currentNode:
            if currentNode.hasleftChild():
                self._put(key,val,currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key,val,parent = currentNode)
        else: 
            if currentNode.hasrighChild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key,val,parent = currentNode)
    
    def __setitem__(self,k,v):
        self.put(k,v);
        
    def get(self, key):
        if (self.root):
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
      
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        
        elif currentNode.key ==key:
            return currentNode
        
        elif key <currentNode.key:
            return self._get(key,currentNode.leftchild)
        else:
            return self._get(key,currentNode.rightchild)
            
    def __getitem__(self, key):
        return self.get(key)
        
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
            
    def delete(self,key):
        if self.size>1:
            nodetoRemove = self._get(key, self.root)
            if nodetoRemove:
                self.remove(nodetoRemove)
                self.size = self.size -1
            else:
                raise KeyError('Error, key not in Tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size -1
        else:
            raise KeyError('Error, Key not in tree')
            
    def __delitem__(self,key):
         self.delete(key)
    
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftchild = None
            else:
                self.parent.rightchild = None
                
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftchild():
                    self.parent.leftchild = self.leftChild
                else:
                    self.parent.rightchild = self.leftchild
                self.leftchild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftchild = self.rightchild
                else: 
                    self.parent.rightchild = self.rightchild
                self.rightchild.parent = self.parent
    
    def findSuccessor(self):
        succ = None
        if self.hasRightchild():
            succ = self.rightchild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightchild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightchild = self
        return succ
        
    def findMin(self):
        current = self
        while current.hasleftchild():
            current = current.leftchild
        return current
        
    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
            else:
               currentNode.parent.rightchild =None
        elif currentNode.hasbothchildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            
        else:
            if  currentNode.hasLeftchild():
                if currentNode.isleftchild():
                    currentNode.leftchild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftchild
                elif currentNode.isrightChild():
                     currentNode.leftchild.parent = currentNode.parent
                     currentNode.parent.rightchild = currentNode.leftchild
                else:
                    currentNode.replacenodeData(currentNode.leftchild.key,
                                                currentNode.leftchild.payload,
                                                currentNode.leftchild.leftchild,
                                                currentNode.leftchild.rightchild)
                 
            else:
                if currentNode.isleftchild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightchild
                elif currentNode.isrightChild():
                    currentNode.isrightChild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.rightchild
                else:
                    currentNode.replacenodeData(currentNode.rightchild.key,
                                            currentNode.rightchild.payload,
                                            currentNode.rightchild.leftchild,
                                            currentNode.rightchild.rightchild)
                     

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
                
        
        
        