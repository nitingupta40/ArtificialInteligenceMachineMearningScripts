# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:52:21 2015

@author: nitin
"""

class solution:
    def addTwoNumber(self, l1,l2):
        head = temp = ListNode(0)
        carry =0
    
        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            tempSum = temp1 + temp2 +carry
            
            temp.next = ListNode(tempSum%10)
            temp = temp.next
            carry = temp //10
            
            if l1:
                l1 = l1.next
            if l2:
                ll2 = l2.next
        return head.next
            
            