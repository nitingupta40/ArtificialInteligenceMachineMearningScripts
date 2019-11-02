# -*- coding: utf-8 -*-
"""
Created on Wed May 06 11:01:06 2015

@author: nitin
"""

class BstNode:
    def __init__ (self):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.root = None

    def find_recursive(self, node, key):
        if None == key or key == node.key:
            return node
        elif key < node.key:
            return self.find_recursive(node.left, key)
        else:
            return self.find_recursive(node.right, key)

    def find_iterative(self, node, key):
        current_node = node
        while current_node:
            if key  == current_node.key:
                return current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
            return None

    def search(self, key):
        return self.find_iterative(self.root,key)
    
    def insert(self, key, value):
        if None == self.root:
           self.root =BstNode(key,value)
           return True
        current_node =self.root
        while current_node:
            if key == current_node.key:
                print "The key does exists"
                return False
            elif key <= current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BstNode(key, value, current_node)
                    return True
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BstNode(key, value, current_node)
                    return True
                    
                    
                    
                        
                
                
            
        
            
                
        