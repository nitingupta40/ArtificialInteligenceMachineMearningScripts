# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:04:28 2015

@author: nitin
"""

from bs4 import BeautifulSoup
import urllib2
import re

chare = re.compile(r'[!-\.&]') 
itemowners ={}
dropwords =['a','new','some','more','my','own','the','many','other','another']
currentuser = 0 
for i in range (1,51):
    c=  urllib2.urlopen('http://member.zebo.com/Main?event_key=USERSEARCH&wiowiw=wiw&keyword=car&page=%d' %(i))
    soup = BeautifulSoup(c.read())
    for td in soup('td'):
        if ('class' in dict(td.attrs) and td['class'] =='bgverdanasmall'):
            items = [re.sub(chare,'',a.contents[0].lower()).strip() for a in td('a')]
            for item in items:
                txt = ' '.join([t for i in item.split(' ') if t not in dropwords])
                if len(txt)<2: continue
                itemowners.setdefault(txt,{})
                itemowners[txt][currentuser] =1
        currentuser+=1
 
