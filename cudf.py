# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:16:51 2015

@author: nitin
"""
import math
import random
import re
_pck_list =[]
_pck_name =[]
_pck_version =[]
_pck_depends=[]
_pck_conflicts =[]
_pck_provides =[]
_pck_number =[]
_pck_source=[]
_pck_sourceversion =[]
_pck_recommends =[]
_pck_replace =[]

class Package(object):
    def __init__(self, _pck_name =None, _pck_version =None, _pck_depends =None, _pck_conflicts =None, 
                    _pck_provides =None, _pck_number =None, _pck_source =None, _pck_sourceversion =None,
                    _pck_recommends =None, _pck_replace =None):
        self._pck_name = _pck_name
        self._pck_version = _pck_version
        self._pck_depends = _pck_depends
        self._pck_conflicts = _pck_conflicts
        self._pck_provides = _pck_provides
        self._pck_number = _pck_number
        self._pck_source = _pck_source
        self._pck_sourceversion = _pck_sourceversion
        self._pck_recommends = _pck_recommends
        self._pck_replace = _pck_replace
    
def _fn_readfile():
    __file =[]
    count =0
    num =0
    _file = open("C:\\Users\\nitin\\Desktop\\new1.txt","r")
    for f in _file:
        if f:
            if re.search("package:",f):
                __pck_name =(f.replace("package:",''))
                #print __pck_name
            elif re.search("sourceversion:",f):
                if (f[6] =='v'):
                    __pck_sourceversion = (f.replace("sourceversion:",''))
                else:
                    pass
            elif re.search("version:",f):
                if (f[0] =='v'):
                    __pck_version =(f.replace("version:",''))
                    if __pck_version.count ==0:
                        __pck_version = ""
                else:
                    pass
            elif re.search("depends:",f):
                __pck_depends =(f.replace("depends:",''))
            elif re.search("conflicts:",f):
                __pck_conflicts = (f.replace("conflicts:",''))
            elif re.search("provides:",f):
                __pck_provide = (f.replace("provides:",''))
            elif re.search("number:",f):
                __pck_number = (f.replace("number:",''))
            elif re.search("source:",f):
                __pck_source = (f.replace("source:",''))
            elif re.search("recommends:",f):
                __pck_recommends= (f.replace("recommends:",''))
            elif re.search("replace:",f):
                __pck_replace=(f.replace("replace"))
                if __pck_replace.count ==0:
                    __pck_replace =""
            else:
                continue

        if (not f):
            pass
    print __pck_name,__pck_sourceversion,__pck_version,__pck_depends,__pck_conflicts,__pck_provide,__pck_number,__pck_source,__pck_recommends,__pck_replace
    _file.close()
def _fn_savefile():
        
        
                #print __pck_sourceversion.split()
        #print __pck_version
#            print __pck_name.split(),__pck_version.split(),__pck_depends.split(),__pck_conflicts.split(),__pck_provide.split(),__pck_number.split(),__pck_source.split(),__pck_sourceversion.split(),__pck_recommends.split()
            _pck_list.append(Package(__pck_name.split(),__pck_version.split(),__pck_depends.split(),
                             __pck_conflicts.split(),__pck_provide.split(),__pck_number.split(),
                             __pck_source.split(),__pck_sourceversion.split(),__pck_recommends.split(),
                             __pck_replace.split()))

    
_fn_readfile()



