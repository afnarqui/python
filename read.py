#!/usr/bin/env python
# coding: utf-8

# # Carga de datos a través de la función read_csv

# In[16]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[17]:


import pandas as pd
import IPython
print(IPython.sys_info())


# In[20]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[21]:


get_ipython().system('ls')


# In[23]:


dir = '/home/jovyan/python/dataset/{}'.format('data.csv')
data = pd.read_csv(dir)


# In[24]:


data.head()


# In[ ]:




