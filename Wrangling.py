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


# In[23]:


data[1:25]


# In[24]:


data[10:35]


# In[26]:


data[:8] # es lo mismo que data[1:8]


# In[27]:


data[60:]


# In[29]:


data[3330:]


# In[33]:


## Usuarios con Total Mins > 300
data1 = data[data["Day Mins"] > 300]
data1


# In[34]:


## Usuarios de Nueva york (State = "NY")
data2 = data[data["State"]=="NY"]
data2


# In[38]:


##AND -> &
data3 = data[(data["State"]=="NY") & (data["Day Mins"]> 300)]
data3.shape


# In[41]:


##OR -> |
data4 = data[(data["Day Mins"]>300) | (data["State"]=="NY")]
data4.shape
data4.head()


# In[42]:


data5 = data[data["Day Calls"]< data["Night Calls"]]
data5.shape


# In[43]:


data6 = data[data["Day Mins"]< data["Night Mins"]]
data6.shape


# In[48]:


##Minutos de día , de noche y Longitud de la Cuenta de los primeros 50 individuos
## primero columnas y luego las filas
subset_first_50 = data[["Day Mins", "Night Mins", "Account Length"]][:50]
subset_first_50.shape
subset_first_50.head()


# In[49]:


subset.head()


# In[50]:


subset[:10]


# In[55]:


## primero las filas y luego las columnas
data.iloc[1:10,3:6]


# In[56]:


data.iloc[:,3:6] ## Todas las filas para las columnas entre la 3 y la 6
data.iloc[1:10,:] ## Todas las columnas para las filas de la 1 a la 10


# In[57]:


data.iloc[1:10, [2,5,7]]


# In[58]:


data.iloc[[1,5,8,36],[2,5,7]]


# In[60]:


data.loc[[1,5,8,36],["Area Code", "VMail Plan", "Day Mins"]]


# In[62]:


data["Total Mins"] = data["Day Mins"] + data["Night Mins"] + data["Eve Mins"]


# In[64]:


data["Total Mins"].head()


# In[65]:


data["TotalCalls"] = data["Day Calls"] + data["Night Calls"] +data["Eve Calls"]


# In[66]:


data.shape


# In[67]:


data.head()


# In[ ]:




