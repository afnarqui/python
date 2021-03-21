#!/usr/bin/env python
# coding: utf-8

# # Carga de datos a través de la función read_csv

# In[16]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[57]:


import pandas as pd
import numpy as np
import IPython
import os
print(IPython.sys_info())


# In[70]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[72]:


get_ipython().system('ls')


# In[74]:


dir = '/home/jovyan/python/dataset/{}'.format('data.csv')
dir2 = '/home/jovyan/python/dataset/'
file = 'Customer Churn Columns.csv'
fullpath = os.path.join(dir2, file)
data = pd.read_csv(dir, sep = ",", dtype={"pclass": np.float64}, header=0, names=None, index_col=None, na_filter=False)


# In[68]:


data.head()
data.columns.values


# In[79]:


data_cols = pd.read_csv(fullpath)
data_col_list = data_cols["Column_Names"].tolist()
data2 = pd.read_csv(dir2 + "Tab Customer Churn Model.txt", header = None, names = data_col_list)
data2.columns.values


# In[ ]:




