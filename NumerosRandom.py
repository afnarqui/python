#!/usr/bin/env python
# coding: utf-8

# ### Generación aleatoria de números

# In[24]:


import numpy as np
import pandas as pd


# ##Generar un número aleatoria entero entre 1 y 100

# In[3]:


np.random.randint(1,100)


# ##La forma más clásica de generar un número aleatorio es entre 0 y 1 (con decimales)

# In[4]:


np.random.random()


# In[6]:


##Función que genera una lista de n números aleatorios enteros dentro del intervalo [a,b]
def randint_list(n, a, b):
    x = []
    for i in range(n):
        x.append(np.random.randint(a, b))
    return x


# In[9]:


randint_list(25, 1, 50)


# In[10]:


import random


# In[11]:


random.randrange(1, 100)


# In[14]:


for i in range(10):
    print(random.randrange(0, 100, 7))


# In[17]:


a = np.arange(100)
a


# In[19]:


np.random.shuffle(a)
a


# In[21]:


cd


# In[22]:


ls


# In[25]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')
data = pd.read_csv(dir)


# In[26]:


data.head()


# In[27]:


data.shape


# In[28]:


data["Total Mins"] = data["Day Mins"] + data["Night Mins"] + data["Eve Mins"]


# In[29]:


data["Total Mins"].head()


# In[30]:


data["TotalCalls"] = data["Day Calls"] + data["Night Calls"] +data["Eve Calls"]


# In[31]:


data.shape


# In[32]:


data.head()


# In[33]:


column_list = data.columns.values.tolist()
column_list


# In[38]:


np.random.choice(column_list)


# ### Seed

# In[40]:


np.random.seed(2021)
for i in range(5):
    print(np.random.random())


# ### Funciones de distribución de probabilidades
# 
# Distribución Uniforme

# In[52]:


a = 1
b = 100
n = 100000
data = np.random.uniform(a, b, n)


# In[53]:


import matplotlib.pyplot as plt


# In[54]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(data)


# ## Distribución Normal

# In[62]:


data = np.random.randn(1000000)


# In[63]:


x = range(1, 1000001)
plt.plot(x, data)


# In[64]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(data)


# In[65]:


plt.plot(x, sorted(data))


# In[67]:


mu =5.5
sd = 2.5
z_10000 = np.random.randn(10000)
data = 5.5 + 2.5 *z_10000  # z = (x -mu) / sd -> N(0,1), x = mu + sd * z
plt.hist(data)


# In[68]:


data = np.random.randn(2, 4)
data


# In[ ]:




