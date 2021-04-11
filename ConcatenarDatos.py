#!/usr/bin/env python
# coding: utf-8

# # Concatenar y apendizar data sets

# In[2]:


import pandas as pd


# In[3]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")
get_ipython().run_line_magic('ls', '')
dir = '/home/jovyan/python/dataset/{}'.format('winequality-red.csv')
dir_white = '/home/jovyan/python/dataset/{}'.format('winequality-white.csv')


# In[4]:


red_wine = pd.read_csv(dir, sep=";")


# In[5]:


red_wine.head()


# In[6]:


red_wine.columns.values


# In[7]:


red_wine.shape


# In[8]:


white_wine = pd.read_csv(dir_white, sep = ";")


# In[9]:


white_wine.columns.values


# In[10]:


white_wine.shape


# ### En python, tenemos dos tipos de jes,
# * axis = 0 denota el eje horizontal
# * axis = 1 denota el eje vertical

# In[11]:


wine_data = pd.concat([red_wine, white_wine], axis = 0)


# In[12]:


wine_data.shape


# In[13]:


wine_data.head()


# In[14]:


data1 = wine_data.head(10)
data2 = wine_data[300:310]
data3 = wine_data.tail(10)


# In[15]:


wine_scramble = pd.concat([data1, data2, data3], axis = 0)


# In[16]:


wine_scramble


# In[17]:


wine_scramble = pd.concat([data2, data1, data3], axis=0)
wine_scramble


# ### Datos distribuidos

# In[18]:


dir_distributed = '/home/jovyan/python/dataset/distributed-data/{}'.format('001.csv')
data = pd.read_csv(dir_distributed)


# In[19]:


data.head()


# In[20]:


data.shape


# * Importar el primer fichero
# * Hacemos un bucle para ir recorriendo todos y cada uno de los ficheros. 
#      * Importante tener una consistencia en el nombre de los ficheros
#      * Importamos los ficheros uno a uno
#      * Cada uno de ellos debe apendizarse (añadirse al final) del primer fichero que ya habíamos cargado
# * Repetimos el bucle hasta que no queden ficheros

# In[21]:


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
    


# In[22]:


data.shape


# In[23]:


data.tail()


# In[24]:


data.head()


# In[25]:


final_length


# In[26]:


final_length == data.shape[0]


# # Joins de datasets

# In[27]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset/athletes/'")
get_ipython().run_line_magic('ls', '')
filepath = '/home/jovyan/python/dataset/athletes/'
data_main = pd.read_csv(filepath + 'Medals.csv', encoding= "ISO-8859-1")


# In[28]:


data_main.head()


# In[29]:


a = data_main["Athlete"].unique().tolist()


# In[30]:


len(a)


# In[31]:


data_main.shape


# In[32]:


data_country = pd.read_csv(filepath+"Athelete_Country_Map.csv", encoding= "ISO-8859-1")


# In[33]:


data_country.head()


# In[34]:


data_country.shape


# In[35]:


len(data_country)


# In[36]:


data_country[data_country["Athlete"] == "Aleksandar Ciric"]


# In[37]:


data_sports = pd.read_csv(filepath+"Athelete_Sports_Map.csv")


# In[38]:


data_sports.head()


# In[39]:


len(data_sports)


# In[40]:


data_sports[(data_sports["Athlete"]== "Chen Jing") | 
            (data_sports["Athlete"] == "richard Thompson") | 
            (data_sports["Athlete"] == "Matt Ryan")]


# In[41]:


data_country_dp = data_country.drop_duplicates(subset="Athlete")
len(data_country_dp)


# In[42]:


data_main_country = pd.merge(left = data_main, right = data_country_dp, 
                             left_on = "Athlete", right_on = "Athlete")


# In[43]:


data_main_country.head()


# In[44]:


data_main_country.shape


# In[45]:


data_main_country[data_main_country["Athlete"] == "Aleksandar Ciric"]


# In[46]:


data_sports_dp = data_sports.drop_duplicates(subset="Athlete")


# In[47]:


len(data_sports_dp)  == len(a)


# In[48]:


data_final = pd.merge(left= data_main_country, right=data_sports_dp,
                      left_on ="Athlete", right_on = "Athlete")


# In[49]:


data_final.head()


# In[50]:


data_final.shape


# ### Tipos de Joins

# In[51]:


from IPython.display import Image
import numpy as np


# ***Inner join <= A (Left join), B (Right join) <= Outer Join***

# ### Inner join
#  * Devuelve un data frame con las filas que tienen valor tanto en el primer como en el segundo data frame que estamos uniendo
#  * El número de filas será igual al número de filas **comunes** que tengan ambos data sets
#      * Data Set A tiene 60 filas
#      * Data Set B tiene 50 filas
#      * Ambos comparten 30 filas
#      * Entocnes A Inner join B tendrá 30 filas
#  * En términos de teoría de conjuntos, se trata de la intersección de los dos conjuntos

# In[52]:


get_ipython().run_line_magic('cd', '"/home/jovyan/python/resources"')
get_ipython().run_line_magic('ls', '')
dirImageJoin =  "/home/jovyan/python/resources/inner-join.png"
dirImageLeft =  "/home/jovyan/python/resources/left-join.png"
dirImageRight =  "/home/jovyan/python/resources/right-join.png"
dirImageOuter =  "/home/jovyan/python/resources/outer-join.png"


# In[53]:


Image(filename=dirImageJoin)


# ### Left join
#  * Devuelve un data frame con las filas que tuvieran valor en el dataset de la izquierda, sin importar si tienen correspondencia en el de la izquierda o no.
#  * El número de filas será igual al número de filas **del data frame izquierdo**
#      * Data Set A tiene 60 filas
#      * Data Set B tiene 50 filas
#      * Entonces A Right join B tendrá 50 filas
#  * En términos de teoría de conjuntos, se trata del propio data set de la derecha quien, además tiene la intersección en su interior

# In[54]:


Image(filename=dirImageLeft)


# ### Right join
#  * Devuelve un data frame con las filas que tuvieran valor en el dataset de la derecha, sin importar si tienen correspondencia en el de la derecha o no.
#  * El número de filas será igual al número de filas **del data frame izquierdo**
#      * Data Set A tiene 60 filas
#      * Data Set B tiene 50 filas
#      * Entonces A Left join B tendrá 60 filas
#  * En términos de teoría de conjuntos, se trata del propio data set de la izquierda quien, además tiene la intersección en su interior

# In[55]:


Image(filename=dirImageRight)


# ### Outer join
#  * Devuelve un data frame con todas las filas de ambos, reemplazando las ausencias de uno o de otro con Nas en la región específica.
#  * La filas del data frame final que no correspondan a ninguna fila del data frame derecho(o izquierdo), tendrán Nas en las columnas del data frame derecho(o izquierdo)
#  * El número de filas será igual al **máximo número de filas de ambos data frames**
#      * Data Set A tiene 60 filas
#      * Data Set B tiene 50 filas
#      * Entonces A Outer join B tendrá 80 filas
#  * En términos de teoría de conjuntos, se trata de la unión de conjuntos

# In[56]:


Image(filename=dirImageOuter)


# In[58]:



out_athletes = np.random.choice(data_main["Athlete"], size = 6, replace = False)


# In[71]:


data_country_dlt = data_country_dp[(-data_country_dp["Athlete"].isin(out_athletes))
                                   & 
                                   (data_country_dp["Athlete"] != "Michael Phelps")
                                  ]

data_sports_dlt = data_sports_dp[(-data_sports_dp["Athlete"].isin(out_athletes))
                                   & 
                                   (data_sports_dp["Athlete"] != "Michael Phelps")]

data_main_dlt = data_main[(-data_main["Athlete"].isin(out_athletes))
                                   & 
                                   (data_main["Athlete"] != "Michael Phelps")]


# In[66]:


len(data_country_dlt) - len(data_country_dp)


# In[72]:


len(data_country_dlt) 


# In[73]:


len(data_sports_dlt) 


# In[75]:


len(data_main) 


# In[77]:


#data_main contiene toda la info
#data_country_dlt le falta la info de 7 atletas
len(data_country_dlt)  -  len(data_main) 
merged_inner = pd.merge(left = data_main, right = data_country_dlt, how= "inner", left_on = "Athlete", right_on = "Athlete")


# In[79]:


len(merged_inner)


# In[80]:


merged_inner.head()


# In[ ]:




