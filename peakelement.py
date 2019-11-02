# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:18:05 2015

@author: nitin
"""

class solution:
    def findPeakElement(self, num):
        l,r = 0,len(num)-1
        while l<r :
            mid = (l+r)/2
            if num[mid] < num[mid+1]:
                l = mid+1
            elif num[mid] >num[mid +1]:
                r = mid
        return r