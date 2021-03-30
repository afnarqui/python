#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Dummy Data Sets

# In[6]:


n = 1000000
data = pd.DataFrame(
    {
        'A' : np.random.randn(n),
        'B' : 1.5 + 2.5 * np.random.randn(n),
        'C' : np.random.uniform(5, 32, n)
    }
)


# In[8]:


data.describe()


# In[9]:


plt.hist(data["A"])


# In[10]:


plt.hist(data["B"])


# In[11]:


plt.hist(data["C"])


# In[12]:


cd 


# In[16]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')
data = pd.read_csv(dir)


# In[17]:


data.head()


# In[18]:


colum_names = data.columns.values.tolist()


# In[19]:


a = len(colum_names)


# In[20]:


a


# In[24]:


new_data = pd.DataFrame({
    'Column Name': colum_names,
    'A': np.random.randn(a),
    'B': np.random.uniform(0, 1, a)
}, index = range(42, 42 + a))


# In[25]:


new_data


# In[ ]:




