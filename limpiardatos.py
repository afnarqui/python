# -*- coding: utf-8 -*-
"""LimpiarDatos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SriluOTO23wBRd_QJndIpY1cJ_qnWD7T
"""

# Importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



"""Cargar datos en un pandas dataframe traer base de datos"""

from google.colab import drive
drive.mount('/content/drive')

# %cd '/content/drive/MyDrive/python/datos/datosp'
!ls

dir = '/content/drive/MyDrive/python/datos/datosp/{}'.format('datosp2.csv')

data = pd.read_csv(dir, encoding='utf-8')

data.head()

type(data)

# visaulizamos las columnas
data.columns

data.index

columna1 = data['movie_title']

columna1.head()

data = data[['movie_title','production_budget','worldwide_gross']]
data

data.shape

dir = '/content/drive/MyDrive/python/datos/datosp/{}'.format('datosp.csv')

datam = pd.read_csv(dir, encoding='utf-8')

datam.shape

num = (datam.dtypes == float) | (datam.dtypes == int)
num

num_cols = [c for c in num.index if num[c]]

num_cols

datamn = datam[num_cols]

datamn

datam['movie_title']

pd.concat([datamn,datam['movie_title']], axis=1)

datamn = pd.concat([datamn,datam['movie_title']], axis=1)

datamn

pd.merge(data, datamn, on='movie_title', how='left')

data2 = pd.merge(data, datamn, on='movie_title', how='left')

data2.shape

