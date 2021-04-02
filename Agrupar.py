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


# ### Operaciones sobre datos agrupados

# In[33]:


double_group.sum()


# In[34]:


double_group.mean()


# In[35]:


double_group.size()


# In[36]:


double_group.describe()


# In[38]:


grouped_income = double_group["Income"]


# In[39]:


grouped_income.describe()


# In[40]:


double_group.aggregate(
    {
        "Income": np.sum,
        "Age": np.mean,
        "Height": np.std
    }
)


# In[41]:


double_group.aggregate(
    {
        "Age" : np.mean,
        "Height" : lambda h:np.mean(h)/np.std(h)
    }
)


# In[42]:


double_group.aggregate([np.sum, np.mean, np.std])


# In[43]:


double_group.aggregate([lambda x: np.mean(x) / np.std(x)])


# ### Filtrado de datos

# In[44]:


double_group.sum()


# In[45]:


double_group["Age"].filter(lambda x: x.sum() > 2496)


# ### Transformación de variables

# In[49]:


zscore = lambda x : (x - x.mean() ) / x.std()


# In[52]:


z_group = double_group.transform(zscore)


# In[53]:


plt.hist(z_group["Age"])


# In[54]:


fill_na_mean = lambda x : x.fillna(x.mean())


# In[55]:


double_group.transform(fill_na_mean)


# ### Operaciones diversas muy útiles

# In[56]:


double_group.head(1)


# In[57]:


double_group.tail(1)


# In[58]:


double_group.nth(32)


# In[59]:


double_group.nth(82)


# In[61]:


data_sorted = data.sort_values(["Age", "Income"])


# In[62]:


data_sorted.head()


# In[63]:


age_grouped = data_sorted.groupby("Gender")


# In[64]:


age_grouped.head()


# In[65]:


age_grouped.tail(1)


# In[66]:


age_grouped.head(1)


# In[ ]:




