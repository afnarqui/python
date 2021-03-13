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

[![N|Solid](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fjupyter.JPG?alt=media&token=474a1a51-3ae5-4c25-9ecc-47e3b0e40c3f)](https://firebasestorage.googleapis.com/v0/b/sistemaadministrativodenegocio.appspot.com/o/python%2Fjupyter.JPG?alt=media&token=474a1a51-3ae5-4c25-9ecc-47e3b0e40c3f)
