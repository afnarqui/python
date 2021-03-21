#!/usr/bin/env python
# coding: utf-8

# ### Plots y visualización de los datos

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('cd', "'/home/jovyan/python/dataset'")


# In[5]:


ls


# In[14]:


dir = '/home/jovyan/python/dataset/{}'.format('data4.txt')
data = pd.read_csv(dir)


# In[19]:


data.head(2)


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


#savefig("path_donde_guardar_id.jpg")


# ### Scatter Plot

# In[18]:


data.plot(kind="scatter", x="Day Mins", y="Day Charge")


# In[21]:


data.plot(kind="scatter", x="Night Mins", y="Night Charge")


# In[28]:


figure, axs = plt.subplots(2,2, sharey=True, sharex= True)
data.plot(kind="scatter", x="Day Mins", y = "Day Charge", ax=axs[0][0])
data.plot(kind="scatter", x="Night Mins", y = "Night Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Day Calls", y = "Day Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y = "Night Charge", ax=axs[1][1])


# ### Histogramas de frecuencias

# ### Regla de Sturges
# ##### La regla de Sturges, propuesta por Herbert Sturges en 1926, es una regla práctica acerca del número de clases que deben considerar al elaborarse un histograma.1​
# 
# Este número viene dado por la siguiente expresión:
# 
# {\displaystyle c=1+\log _{2}(M)}{\displaystyle c=1+\log _{2}(M)}, donde M es el tamaño de la muestra.

# In[47]:


k = int(np.ceil(1+np.log2(3333)))
plt.hist(data["Day Calls"], bins = k)
plt.xlabel("Número de llaamada al día")
plt.ylabel("Frecuencia")
plt.title("Histograma de número de llamadas al día")


# In[37]:


data.shape


# In[39]:


np.log2(2)


# In[40]:


1+np.log2(3333)


# In[44]:


k = int(np.ceil(1+np.log2(3333)))


# In[45]:


k


# ### Boxplot, diagrama de caja y bigotes

# In[51]:


plt.boxplot(data["Day Calls"])
plt.ylabel("Número de llamadas diarías")
plt.title("Boxplot de las llamadas diarías")


# In[52]:


data["Day Calls"].describe()


# In[53]:


IQR = data["Day Calls"].quantile(0.75)-data["Day Calls"].quantile(0.25)


# In[54]:


IQR


# In[55]:


data["Day Calls"].quantile(0.25)- 1.5 * IQR


# In[ ]:




