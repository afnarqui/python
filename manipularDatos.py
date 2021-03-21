#!/usr/bin/env python
# coding: utf-8

# # Resumen de los datos: dimensiones y estructuras

# In[1]:


import pandas as pd


# In[12]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[13]:


ls


# In[8]:


dir = '/home/jovyan/python/dataset/{}'.format('data.csv')


# In[9]:


data = pd.read_csv(dir)


# In[10]:


data.head()


# In[ ]:




