# Michene Learning Data Science en Python

Este proyecto permite trabajar con machine learning data science

## Forma de ejecutar el proyecto en desarrollo

- instalación: `debe estar instalado docker`

## Importante
# con estos pasos vamos a lograr tener el ambiente de jupyter


````bash
  # creamos un volumen en nuestro disco en este caso en el disco d en la carpeta development
  docker run --name datos -v d:/development:/d busybox
  # ejecutamos la imagen de jupyter con el volumen creado anteriormente
  docker run -p 8888:8888 --volumes-from datos -v d:/development:/d jupyter/minimal-notebook
  # entramos al navegador con la ip y el token que nos genero el contenedor en este caso esta:
  http://127.0.0.1:8888/?token=82d118f52a25434ad2726e48950e3ffb52e984c83c81e348
  # nos conectamos el contenedor
  docker exec -ti jupyter bin/bash
  # ejecutamos los paquetes necesarios para trabajar machine learning
  pip3 install pandas
  pip3 install numpy
  pip3 install matplotlib
  pip3 install IPython
  pip3 install scikit-learn
````

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fregresionlineal.JPG?alt=media&token=16f4860a-980d-4125-8307-6fe94311d2ae)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fregresionlineal.JPG?alt=media&token=16f4860a-980d-4125-8307-6fe94311d2ae)

## Terminología
````bash
Datos tabulares = Datos en dos dimensiones.
Líneas = Ejemplos
Columnas = Feature. Estas son importantes por que nos van a ayudar a predecir cosas gracias a los modelos que usemos de Machine Learning
Cantidad de columnas = Dimensión de los datos
Output de un algoritmo de Machine Learning (ML) = modelo
Variable objetivo = Target
````

## El ciclo de Machine Learning
````bash
Definición del problema
Preparación de los datosn   limpiar datos, modificarlos, transformarlos
Representación de los datos 
Modelamiento / Algoritmos de ML regresión lineal, arbol de regresión etc
Evaluación
````

## Numpy
````bash
es una librería muy importante para el ecosistema de Python ya que es la base de todos los cálculos cientificos y
muchas de las librerías de Michine Learning.
np.linspace(a,b,n) es una función que permite crear arrays de una dimensión, de largo n, y que contienen puntos entre a y b, distanciados
de forma regular, La distancia entre cada punto sera de (b-a)/(n-1)
shape define la dimensión
Reshaping permite modificar la estructura de los array
Slicing obtener una parte del array que se esta trabajando
Operaciones aritméticas en Numpy
+ ufunc np.add
- ufunc np.subtract
* ufunc np.multiply
np.exp(n) #exponencial
np.log(n) # logarítmo natural
np.sqrt(n) # raiz cuadrada
np.greater(n,m) # superior o igual punto a punto
universal functions ufuncs corren a velocidad de código compilado C.
De poder utilizarse se deberían preferir a el uso de for loops.
Un código Numpy solo con funciones nativas, sin bucles, se le llama código "vectorizado".
Siempre que se pueda ejecutar el código con Numpy ya que este corre en C y es mil veces más rapido que un for loops que corre en python
````

## Cargar datos
````bash
las Librerías son
Numpy
Pandas
Matplotlib.pyplot
Seaborn
pd.read_css es el metodo que nos permite importar lso datos desde un CSV y cargarlo en un DataFrame, que es la estructura de base de Pandas
from google.colab import drive
drive.mount('/content/drive')
%cd '/content/drive/MyDrive/python/datos/datosp'
!ls
dir = '/content/drive/MyDrive/python/datos/datosp/{}'.format('datosp.csv')
data = pd.read_csv(dir, encoding='utf-8')
data.head()
type(data)
````

## Datos desde github
````bash
  data = 
  pd.read_csv('https://github.com/afnarqui/python/dev/datos/valores.csv?raw=true', encoding='utf-8')
  type(data)
````

## DataFrame
````bash
  se debe conocer cuantas lineas y columnas tiene nuestro dataframe
  Un dataframe es una estructura de datos que se compone de los siguientes elementos
  tiene un index general y un index de columnas
  visaulizamos las columnas
  data.columns
````

## Inspección de los tipos de datos
````bash
  la inspección de los datos se da para tener conocimiento de la salud de lso datos que tenemos,
  saber si vienen limpios o no, y también porque se quiere tener un entendimiento
  cuantitativo de ellos. Parte de esto es mirar gráficos estadisticos y enteneder diferentes propiedades numerícas de las columnas
  A diferencia de Numpy, Pandas no solo permite cargar datos numéricos, sino también datos de texto.
  El método info nos va a mostar la cantidad completa de columnas con la cantidad de elementos no nulos que hay en esas columnas y por último muestra el tipo de cada columna
  data.info
  data.dtypes
````


## Estadísticas de las columnas númericas
````bash
  data[num_cols]
  data_num = data[num_cols]
  data_num
  data_num.describe()
  data_num['duration'].hist()
````

## Limpiar datos
````bash
  pd.concat me permite unir datos
  data2.notnull() si sale False es por que faltan datos
  help(pd.Series.value_counts) permite ver la documentación
  Carga de datos a través de la función read
````

## Variables dummy
````python
data["sex"]
dummy_sex = pd.get_dummies(data["sex"], prefix="sex")
dummy_sex.head()

def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name],prefix=var_name)
    df = df.drop(var_name, axis = 1)
    df = pd.concat([df, dummy], axis = 1)
    return df
````
### Plots y visualización de los datos

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fplot.JPG?alt=media&token=a2a91614-153e-4db4-9bd2-cba636a0c55a)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fplot.JPG?alt=media&token=a2a91614-153e-4db4-9bd2-cba636a0c55a)

### Histogramas de frecuencias

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fhistogramadefrecuencia.JPG?alt=media&token=028d358a-2e98-4205-8289-b78c5b7c4aa4)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fhistogramadefrecuencia.JPG?alt=media&token=028d358a-2e98-4205-8289-b78c5b7c4aa4)

### Boxplot, diagrama de caja y bigotes

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2FBoxplot.JPG?alt=media&token=3a6d384c-e419-42d3-bc25-474ab73d1b2f)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2FBoxplot.JPG?alt=media&token=3a6d384c-e419-42d3-bc25-474ab73d1b2f)

### Data Wrangling

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fchuleta1.jpg?alt=media&token=5c443d8a-c36c-4a87-82a4-c2b56a6abe45)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fchuleta1.jpg?alt=media&token=5c443d8a-c36c-4a87-82a4-c2b56a6abe45)

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fchuleta2.jpg?alt=media&token=6d35cf85-50f3-4945-8851-49676613011c)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fchuleta2.jpg?alt=media&token=6d35cf85-50f3-4945-8851-49676613011c)

````python
a = set(desired_columns)
b = set(all_columns_list)
sublist = b-a
sublist = list(sublist)
````

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Ffunciondeprobabilidades.JPG?alt=media&token=14d36d9a-d025-4181-be7a-1e63b9c906d4)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Ffunciondeprobabilidades.JPG?alt=media&token=14d36d9a-d025-4181-be7a-1e63b9c906d4)


[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fladistribucionuniforme.JPG?alt=media&token=9b9c09eb-78a8-44db-8ac2-282ee4241588)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fladistribucionuniforme.JPG?alt=media&token=9b9c09eb-78a8-44db-8ac2-282ee4241588)

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fcampanadegauss.JPG?alt=media&token=4bd51934-2c8c-4f9a-a1ad-5b37ada61790)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fcampanadegauss.JPG?alt=media&token=4bd51934-2c8c-4f9a-a1ad-5b37ada61790)
