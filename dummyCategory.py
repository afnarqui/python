#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Agregación de datos por categoría

# In[2]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')
data = pd.read_csv(dir)


# In[5]:


gender = ["Male", "Female"]
income = ["Poor", "Middle Class", "Rich"]


# In[6]:


n = 500
gender_data = []
income_data = []

for i in range(0, 500):
    gender_data.append(np.random.choice(gender))
    income_data.append(np.random.choice(income))


# In[16]:


income_data[1:5]


# In[17]:


#Z -> N(0,1)
#N(m, s) _> m + s * Z
height = 160 + 30 * np.random.randn(n)  
weight = 65 + 25 * np.random.randn(n) 
age = 30 + 12 * np.random.randn(n)
income = 18000 + 3500 * np.random.rand(n)


# In[18]:


data = pd.DataFrame(
    {
        "Gender": gender_data,
        "Economic Status": income_data,
        "Height": height,
        "Weight": weight,
        "Age": age,
        "Income": income
    }
)


# In[19]:


data.head()


# In[ ]:




