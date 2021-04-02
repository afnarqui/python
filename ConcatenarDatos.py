#!/usr/bin/env python
# coding: utf-8

# # Concatenar y apendizar data sets

# In[1]:


import pandas as pd


# In[31]:


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


# ### Datos distribuidos

# In[32]:


dir_distributed = '/home/jovyan/python/dataset/distributed-data/{}'.format('001.csv')
data = pd.read_csv(dir_distributed)


# In[33]:


data.head()


# In[34]:


data.shape


# * Importar el primer fichero
# * Hacemos un bucle para ir recorriendo todos y cada uno de los ficheros. 
#      * Importante tener una consistencia en el nombre de los ficheros
#      * Importamos los ficheros uno a uno
#      * Cada uno de ellos debe apendizarse (añadirse al final) del primer fichero que ya habíamos cargado
# * Repetimos el bucle hasta que no queden ficheros

# In[47]:


filepath = '/home/jovyan/python/dataset/distributed-data/'
data = pd.read_csv(filepath + '001.csv')
final_length = len(data)
for i in range(2, 333):
    if i < 10:
        filename = "00"+str(i)
    if 10 <= i < 100:
        filename = "0"+str(i)
    if i >= 100:
        filename = str(i)
    file = filepath + filename + ".csv"
    temp_data = pd.read_csv(file)
    final_length += len(temp_data)
    
    data = pd.concat([ data, temp_data], axis= 0)
    


# In[44]:


data.shape


# In[45]:


data.tail()


# In[46]:


data.head()


# In[48]:


final_length


# In[50]:


final_length == data.shape[0]


# # Joins de datasets

# In[58]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset/athletes/'")
get_ipython().run_line_magic('ls', '')
filepath = '/home/jovyan/python/dataset/athletes/'
data_main = pd.read_csv(filepath + 'Medals.csv', encoding= "ISO-8859-1")


# In[54]:


data_main.head()


# In[55]:


a = data_main["Athlete"].unique().tolist()


# In[56]:


len(a)


# In[57]:


data_main.shape


# In[61]:


data_country = pd.read_csv(filepath+"Athelete_Country_Map.csv", encoding= "ISO-8859-1")


# In[62]:


data_country.head()


# In[63]:


data_country.shape


# In[64]:


len(data_country)


# In[65]:


data_country[data_country["Athlete"] == "Aleksandar Ciric"]


# In[66]:


data_sports = pd.read_csv(filepath+"Athelete_Sports_Map.csv")


# In[67]:


data_sports.head()


# In[68]:


len(data_sports)


# In[71]:


data_sports[(data_sports["Athlete"]== "Chen Jing") | 
            (data_sports["Athlete"] == "richard Thompson") | 
            (data_sports["Athlete"] == "Matt Ryan")]


# In[ ]:




