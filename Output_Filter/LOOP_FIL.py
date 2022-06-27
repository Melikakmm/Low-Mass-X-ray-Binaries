#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os 
import pandas as pd

# In[ ]:
#The option below is for interactive mode, therefore if the LOOP_RUN.py is run the file variable should be in comment.
#file = input('Insert the file you wan to filter:')
path_0 = "/tank1/iorio/TEwoc/SEVN_simulations_new/"+file+"/0/"



entries = os.listdir(path_0)


for entry in entries:
    User_file = entry
    if User_file.endswith(".csv"):
        exec(open("/home/martemucci/Filtering/Filter_new.py").read())
        
        
        
    else:
        pass









