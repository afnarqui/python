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


# In[71]:


get_ipython().system('ls')


# In[65]:


dir = '/home/jovyan/python/dataset/{}'.format('data.csv')
file = 'data.csv'
fullpath = os.path.join(dir, file)
data = pd.read_csv(dir, sep = ",", dtype={"pclass": np.float64}, header=0, names=None, index_col=None, na_filter=False)


# In[68]:


data.head()
data.columns.values


# In[ ]:




