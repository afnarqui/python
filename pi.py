#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# * Generamos dos números aleatorios uniforme x e y entre 0 y 1
# * Calcularemos X² + Y²
#     * si el valor es inferior a 1 -> estamos dentro del círculo.
#     * si el valor es superior a 1 -> estamos fuera del círculo.
# * Calculamos el número total de veces que están dentro del círculo y lo dividimos entre el número total de intentos para obtener una aproximación de la probabilidad de caer dentro del círculo.
# * Usamos dicha probabilidad para aproximar el valor de π.
# * Repetimos el experimento un número suficiente de veces (por ejemplo 1000), para obtener (100) diferentes aproximaciones de π.
# * Calculamos el promedio de los n experimentos anteriores para dar un valor final de π.
# 

# In[8]:


def pi_montecarlo(n, n_exp):
    pi_avg = 0

    pi_value_list = []
    for i in range(n_exp):
        value = 0
        x = np.random.uniform(0,1,n).tolist()
        y = np.random.uniform(0,1,n).tolist()
        for j in range(n):
            z = np.sqrt(x[j] * x[j] + y[j] * y[j])
            if z <=1:
                value +=1
        float_value = float(value)
        pi_value = float_value * 4 / n
        pi_value_list.append(pi_value)
        pi_avg += pi_value
    pi = pi_avg /n_exp

    print(pi)
    fig = plt.plot(pi_value_list)
    return (pi, fig)


# In[10]:


pi_montecarlo(10000, 200)


# In[ ]:




