#!/usr/bin/env python
# coding: utf-8

# # Resumen de los datos: dimensiones y estructuras

# In[1]:


import pandas as pd


# In[12]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[14]:


ls


# In[15]:


dir = '/home/jovyan/python/dataset/{}'.format('data3.csv')


# In[16]:


data = pd.read_csv(dir)


# In[19]:


data.head(10)


# In[24]:


urldata = "https://raw.githubusercontent.com/afnarqui/python/dev/dataset/data3.csv"
data2 = pd.read_csv(urldata)


# In[29]:


data.tail()


# In[26]:


data2.head(3)


# In[28]:


data.shape


# In[30]:


data.columns.values


# # Resumen estadísticos básicos con las varialbes numéricas.

# In[32]:


data.describe()


# In[33]:


data.dtypes


# In[34]:


pd.isnull(data["body"])


# In[35]:


pd.notnull(data["body"])


# In[37]:


pd.isnull(data["body"]).values.ravel().sum()


# In[38]:


pd.notnull(data["body"]).values.ravel().sum()


# Los valores que faltan en un data set pueden venir por dos razones:
# * Extracción de los datos
# * Recolección de los datos

# #### Borrado de valores que faltan

# In[40]:


data.dropna(axis=0, how="all")


# In[41]:


data3 = data


# In[42]:


data3.dropna(axis=0, how="any")


# #### Cómputo de los valores faltantes

# In[43]:


data3 = data


# In[44]:


data3.fillna(0)


# In[45]:


data4 = data


# In[46]:


data4.fillna('Desconocido')


# In[47]:


data5 = data


# In[55]:


data5["body"] = data5["body"].fillna(0)
data5["home.dest"] = data5["home.dest"].fillna("Desconocido")
pd.isnull(data5["age"]).values.ravel().sum()


# In[56]:


data5["age"].fillna(data["age"].mean())


# In[57]:


pd.isnull(data5["age"]).values.ravel().sum()


# In[58]:


data5["age"] = data5["age"].fillna(data["age"].mean())


# In[59]:


pd.isnull(data5["age"]).values.ravel().sum()


# In[60]:


data5["age"][1291]


# In[63]:


data5["age"].fillna(method="ffill")


# ### Variables dummy

# In[64]:


data["sex"]


# In[65]:


dummy_sex = pd.get_dummies(data["sex"], prefix="sex")


# In[67]:


dummy_sex.head()


# In[68]:


colum_name = data.columns.values.tolist()


# In[69]:


colum_name


# In[71]:


data.drop(["sex"],axis=1)
data = data.drop(["sex"], axis=1)


# In[72]:


data = pd.concat([data,dummy_sex], axis = 1)


# In[74]:


data.head()


# In[75]:


def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name],prefix=var_name)
    df = df.drop(var_name, axis = 1)
    df = pd.concat([df, dummy], axis = 1)
    return df


# In[77]:


data3
createDummies(data3, "sex")


# In[ ]:




