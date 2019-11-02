# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:42:59 2015

@author: nitin
"""

def azureml_main(frame1):
    import pandas as pd
    bins =[0,2.5,5,7.5,10]
    frame1['wind_cat'] = pd.cut[frame1['wind'], bins]
    return frame1