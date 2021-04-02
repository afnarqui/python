#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[9]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")
get_ipython().run_line_magic('ls', '')


# In[12]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')
data = pd.read_csv(dir)


# In[13]:


data.head()


# In[15]:


gender = ["Male", "Female"]
income = ["Poor", "Middle Class", "Rich"]


# In[16]:


n = 500
gender_data = []
income_data = []

for i in range(0, 500):
    gender_data.append(np.random.choice(gender))
    income_data.append(np.random.choice(income))


# In[17]:


income_data[1:5]


# In[18]:


#Z -> N(0,1)
#N(m, s) _> m + s * Z
height = 160 + 30 * np.random.randn(n)  
weight = 65 + 25 * np.random.randn(n) 
age = 30 + 12 * np.random.randn(n)
income = 18000 + 3500 * np.random.rand(n)


# In[19]:


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


# In[20]:


data.head()


# ### Agrupación de datos

# In[21]:


data.groupby("Gender")


# In[22]:


grouped_gender = data.groupby("Gender")


# In[23]:


grouped_gender.groups


# In[25]:


for names in grouped_gender:
    print(names)


# In[27]:


grouped_gender.get_group("Female")


# In[28]:


double_group = data.groupby(["Gender", "Economic Status"])


# In[29]:


len(double_group)


# In[30]:


for names, groups in double_group:
    print(names)
    print(groups)


# In[ ]:




