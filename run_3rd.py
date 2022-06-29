import pandas as pd
import os

path0 = "/Users/mariam/Desktop/LCP2/project/F_data/"  #change according to the machine
dirs = os.listdir(path0)
for d in dirs:
    if d.startswith("F"):
        dr = path0 + d
        f0 = os.listdir(dr)
        f1 = str(dr)+'/'+str(f0)
        path = f1.replace("[",'').replace("]",'').replace("'",'') #path to give for reading the dataframe
        #df = pd.read_csv(path) 



