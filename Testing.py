#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[2]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")
get_ipython().run_line_magic('ls', '')


# In[9]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.csv')
data = pd.read_csv(dir)


# In[10]:


len(data)


# ### Dividir utilizando la distribución normal

# In[11]:


a = np.random.randn(len(data))


# In[12]:


plt.hist(a)


# In[23]:


check = (a <0.75)


# In[24]:


check


# In[25]:


plt.hist(check.astype(int))


# In[26]:


training = data[check]
testing = data[~check]


# In[27]:


len(training)


# In[28]:


len(testing)


# ### Con la libreria sklearn

# In[31]:


train, test = train_test_split(data, test_size = 0.2)


# In[32]:


len(train)


# In[33]:


len(test)


# In[ ]:




