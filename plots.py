#!/usr/bin/env python
# coding: utf-8

# ### Plots y visualización de los datos

# In[1]:


import pandas as pd


# In[4]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[5]:


ls


# In[12]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')
data = pd.read_csv(dir)


# In[11]:


data.head()


# In[ ]:




