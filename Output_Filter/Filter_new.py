#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
import pandas as pd
import dask.dataframe as dd
import matplotlib as plt
import os


# load a single output_XX.csv files:

# In[32]:


path_0 = "/tank1/iorio/TEwoc/SEVN_simulations_new/"+file+"/0"
#Put the following path in comments when you use the interactive mode:
#User_file =str(input('Insert the file:'))

path = path_0 +'/'+User_file


# In[33]:


#The raw data:
df = pd.read_csv(path, sep=",")




# Select systems that satisfy the following conditions:
# 
# 
# 0. System must be Binary not Singular
# 1. compact object = Neutron stars and Black Holes
# 2. Orbital Period = 1_3 hours
# 3. age = 3- 12 Myr

# In[34]:

#---------------------------------------------------------------------------------
#Filter 0
#filtering Singular systems:
#When the mass of at least one star is nan, the binary does not hold.

f_0_1 = (df.Mass_0 != np.nan)
df=df[f_0_1]
f_0_2 = (df.Mass_1 != np.nan)
df=df[f_0_2]



# In[35]:

#---------------------------------------------------------------------------------
#Filter 1


#Filtering the Binary Systems with compact obejct of Neutron stars or Blackholes:
#one of the stars would be in phase of remnant, Phase= 7.
#with the remnant of [4, 5, 6].

sub1 = df.query("Phase_0 == 7 & Phase_1 == 7 ")
sub2 = df.query("Phase_0 != 7 & Phase_1 != 7 ")
sub3  = df.query("RemnantType_0 not in [4, 5, 6] & RemnantType_1 not in [4, 5, 6]")

f_1 = pd.concat([sub1, sub2, sub3])
df = pd.concat([df, f_1, f_1]).drop_duplicates(keep=False)


#For checking:
#df['Phase_0']
#df['Phase_1']


# In[36]:

#-----------------------------------------------------------------------------------
#Filter 2


#Orbital Period 1-3 hours:

f_2 = (df.Period>=0.000114) & (df.Period<=0.000342)
df=df[f_2]




#Checking:
#df['Period'].unique()


# In[37]:
#-----------------------------------------------------------------------------------
#Filter 3

f_3_1 = df[(df.Phase_0 != 7)&(df.Radius_0>0.8*df.RL0)]
f_3_2 = df[(df.Phase_1 != 7)&(df.Radius_1>0.8*df.RL1)]
f_3 = pd.concat([f_3_1, f_3_2])
df = pd.merge(df, f_3, how = 'inner')



# In[40]:
#-----------------------------------------------------------------------------------
#Filter 4

f_4 = (df.BWorldtime>=3) & (df.BWorldtime<=12)
df=df[f_4]



# In[43]:

#_______----------________----------__________--------


#This is where the data is saved in the virtual machine:

path_1 = '/home/martemucci/Filtering/'
dest = path_1 +'F_data/'+'F_'+file+'/'

df.to_csv(dest+ 'Filtered_'+ User_file)


