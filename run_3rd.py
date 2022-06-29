import pandas as pd
import os
from iterate.py import i
if dirs[i].startswith("F"): #get i from iteration script
    dr = path0 + d
    f0 = os.listdir(dr)
    f1 = str(dr)+'/'+str(f0)
    path = f1.replace("[",'').replace("]",'').replace("'",'') #path to give for reading the dataframe
        #df = pd.read_csv(path)
