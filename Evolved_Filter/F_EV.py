#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This piece of code is filtering the initial condition of the data filtered for Low-Mass X-Ray Binary systems and writes dat files as a csv files :

import pandas as pd
import numpy as np
import os
import csv


# In[ ]:


#I made an ID table specifying the ID of filtered data:
path_0_0 = '/home/martemucci/Filtering/F_data'

path_1 = "/tank1/iorio/TEwoc/SEVN_simulations_new/"

# In[5]:


for res in result:
    if res.startswith('evolved'):
        #modify : evolved_XX_dat
        modify = res.replace('.', '_')
        path_2 = path_1 + raw_folder+'/0/'
        path_3 = path_2 + res
        with open(path_3, 'r') as input_file:
              lines = input_file.readlines()
              newlines = []
              for line in lines:
                   newline = line.strip('').split()
                   newlines.append(newline)
        with open('/home/martemucci/Filtering/F_data/'+'F_'+raw_folder+'/'+raw+res.replace('.dat', '.csv'), 'w') as output_file:
              file_writer = csv.writer(output_file)
              file_writer.writerows(newlines)
                
                
                
    else:
        pass
        
        

