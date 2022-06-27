#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv 
import pandas as pd
import numpy as pd
import os
import csv
import functools as ft

# In[ ]:



path_1 = "/tank1/iorio/TEwoc/SEVN_simulations_new/"

#SEVN contains name of 12 folders with different metalicity and alpha:
SEVN = os.listdir(path_1)



##raw_folder: 12 folders in SEVN like sevn_output_Z0.014A0.5L1:
for raw_folder in SEVN:
    if raw_folder.startswith('sevn_'):
        #e.g : raw = 'Z0_014A0_5'
        raw = raw_folder.replace('.', '_').replace("sevn_output_","" ).replace('L1', '')
        path_2 = path_1 + raw_folder+'/0/'
        result = os.listdir(path_2)
        exec(open("/home/martemucci/Filtering/F_EV.py").read())
        #merging evolved files with csv format:
        dfs = []
        k = 0
        while k<29:
               globals()[raw + 'evolved_{}'.format(k)] = pd.read_csv('/home/martemucci/Filtering/F_data/'+'F_'+raw_folder+'/'+raw + 'evolved_{}.csv'.format(k))
               dfs.append(globals()[raw + 'evolved_{}'.format(k)])
               k = k + 1
        ev_df = ft.reduce(lambda left, right: pd.merge(left, right, how = 'outer'), dfs)
        #Filtering out the stars we are interested by getting the ID from the filtered data and using it to filtered merged evolved files:
        F_dataset = pd.read_csv('/home/martemucci/Filtering/F_data/'+'F_'+raw_folder+'/'+'F'+raw.replace("_",".")+'.csv')
        F_ID = F_dataset['ID']
        
        #Here we filtered stars with the same ID of Filtered data:
        ev_df  = ev_df.loc[ev_df['#ID'].isin(F_ID)]
        final_dataset = 'init_'+raw
        ev_df.to_csv('/home/martemucci/Filtering/F_data/'+'F_'+raw_folder+'/'+final_dataset+'.csv')
       
        #Now we delete the evolved_XX.csv files:
        path_4 = '/home/martemucci/Filtering/F_data/'
        path_5 = path_4 + 'F_'+raw_folder + '/'
        f = os.listdir(path_5)
        for data in f:
            if data.startswith('Z'):
                os.remove(path_5 + data)
            else:
                pass
    
    

