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
````
