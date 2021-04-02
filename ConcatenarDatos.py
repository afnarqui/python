#!/usr/bin/env python
# coding: utf-8

# # Concatenar y apendizar data sets

# In[1]:


import pandas as pd


# In[17]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")
get_ipython().run_line_magic('ls', '')
dir = '/home/jovyan/python/dataset/{}'.format('winequality-red.csv')
dir_white = '/home/jovyan/python/dataset/{}'.format('winequality-white.csv')


# In[13]:


red_wine = pd.read_csv(dir, sep=";")


# In[14]:


red_wine.head()


# In[15]:


red_wine.columns.values


# In[16]:


red_wine.shape


# In[18]:


white_wine = pd.read_csv(dir_white, sep = ";")


# In[19]:


white_wine.columns.values


# In[20]:


white_wine.shape


# ### En python, tenemos dos tipos de jes,
# * axis = 0 denota el eje horizontal
# * axis = 1 denota el eje vertical

# In[21]:


wine_data = pd.concat([red_wine, white_wine], axis = 0)


# In[22]:


wine_data.shape


# In[23]:


wine_data.head()


# In[24]:


data1 = wine_data.head(10)
data2 = wine_data[300:310]
data3 = wine_data.tail(10)


# In[25]:


wine_scramble = pd.concat([data1, data2, data3], axis = 0)


# In[26]:


wine_scramble


# In[27]:


wine_scramble = pd.concat([data2, data1, data3], axis=0)
wine_scramble


# In[ ]:




