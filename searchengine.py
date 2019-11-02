# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:42:50 2015

@author: nitin
"""
import urllib2
from bs4 import *
from urlparse import urljoin
from sqlite3 import dbapi2 as sqlite 
class crawler:
    ignorewords = set(['the','of','to','and','a','in','is','it'])
    def __init__(self, dbname):
        self.con =sqlite.connect(dbname)
    def __del__(self):
        self.con.close()
    def dbcommit(self):
        self.con.commit()
    def getentryid(self,table,field,value,createnew=True):
        return None
    def addtoindex(self,url,soup):
        if self.isindexed(url): return
        print 'Indexing' + url
        text = self.gettextonly(soup)
        words = self.separatewords(text)
        urlid = self.getentryid('urllist','url',url)
        for i in range(len(words)):
            word =words[i]
            if word in ignorewords: continue
            wordid = self.getentryid('wordlist','word',word)
            self.con.execute("insert into wordlocation(urlid,wordid,location)\values(%d,%d,%d)" %(urlid,wordid,i))
        
    def gettextonly(self,soup):
        v = soup.string
        if v ==None:
            c = soup.contents
            resulttext =''
            for t in c:
                subtext = self.gettextonly(t)
                resulttext+=subtext+'\n'
            return resulttext
        else:
            return v.strip()
    def separatewords(self,text):
        splitter = re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s!='']
    def isindexed(self,url):
        return False
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass
    def crawl(self, pages, depth =2):
        for i in range(depth):
            newspages=set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page,soup)
                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page,link['href'])
                        if url.find("'") !=-1: continue
                        url = url.split('#')[0]
                        if url[0:4] =='http' and not self.isindexed(url):
                            newspages.add(url)
                            linkText = self.gettextonly(link)
                            self.addlinkref(page,url,linkText)                            
            self.dbcommit()
        pages = newpages
       
    def createindextbales(self):
        self.con.execute('create table urllist(url)')
        self.con.execute('create table wordlist(word)')
        self.con.execute('create table wordlocation(urlid,wordid,location)')
        self.con.execute('create table link(fromid integer,toid integer)')
        self.con.execute('create table linkwords(wordid,linkid)')
        self.con.execute('create index wordidx on wordlist(word)')
        self.con.execute('crate index urlidx on urllist(url)')
        self.con.execute('create index wordurlidx on wordlocation(wordid)')
        self.con.execute('create index urltoidx on link(toid)')
        self.con.execute('create index urlfromidx on link(fromid)')
        self.dbcommit()        
        