# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:20:38 2015

@author: nitin
"""

class solution:
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    dic,ans, n =set(), set(), len(s)
    for i in xrange(n-4):
        cur = s[i: i+10]
        if cur in dic:
            print(cur)
            ans.add(cur)
        else:
            dic.add(cur)
    print (list(ans))