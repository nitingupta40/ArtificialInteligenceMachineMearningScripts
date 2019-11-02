# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:28:57 2015

@author: nitin
"""

def azureml_main(frame1):
    import matplotlib
    matplotlib.use('agg')
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.tools.plotting import scatter_matrix
    frame1.drop(["X","Y","month","day"], axis =1, inplace =True)
    fig1 = plt.Figure(1, figsize =(12,9))
    ax = fig1.gca()
    scatter_matrix(frame1, alpha = 0.2, figsize=(10,10), diagonal ='kde', ax=ax)
    fig1.savefig('scatter2.png')
    return frame1
    
    
def azureml_main(frame1):
    import pandas as pd
    import os.path
    frame1 = frame1[(frame["FFMC"]> 40.0) & \
                    (frame["ISI"]<30.0) & \
                    (frame1["rain"]<3.0)]
    return frame1