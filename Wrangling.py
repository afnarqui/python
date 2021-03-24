#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[7]:


ls


# In[8]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')


# In[9]:


data = pd.read_csv(dir)


# In[10]:


data.head()


# ### Crear un subconjunto de datos

# In[11]:


account_length = data["Account Length"]


# In[12]:


account_length.head()


# In[13]:


type(account_length)


# In[14]:


subset = data[["Account Length", "Phone", "Eve Charge","Day Calls"]]


# In[15]:


subset.head()


# In[16]:


type(subset)


# In[17]:


desired_columns = ["Account Length", "Phone", "Eve Charge", "Day Calls"]
subset = data[desired_columns]
subset.head()


# In[19]:


desired_columns = ["Account Length", "VMail Message", "Day Calls"]
desired_columns


# In[20]:


all_columns_list = data.columns.values.tolist()
all_columns_list


# In[21]:


sublist = [x for x in all_columns_list if x not in desired_columns]
sublist


# In[22]:


subset = data[sublist]
subset.head()


# In[ ]:




