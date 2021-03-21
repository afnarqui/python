#!/usr/bin/env python
# coding: utf-8

# ### Plots y visualización de los datos

# In[23]:


import pandas as pd
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


# In[ ]:




