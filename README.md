# Práctica de Vectores y Matrices

## Instrucciones Generales
- El archivo **debe** llamarse **Matrices.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**

##	Elemento menor y mayor de la lista
Escriba un programa con sintaxis Python cuya función principal se llame **extremosLista(lista)**, que reciba como entrada una lista con números enteros denominado **lista** y que retorne la lista con 2 elementos donde ellos serán el número menor y mayor de la lista

```python
>>>extremosLista([18,5,8,45,96,60])
[5,96]

>>> extremosLista([96, 96,96])
[96]

>>> extremosLista([])
"Error: La lista debe contener al menos 2 elementos"

>>> extremosLista([2,5,7,"ABC"])
"Error: La lista debe elementos tipo entero"
```

##	Eliminar elementos lista
Escriba un programa con sintaxis Python cuya función principal se llame **eliminarElementosLista(lista1, lista2)**, que reciba como entrada dos listas con números enteros denominado, donde **lista2** contiene los elementos a eliminar de **lista1** y que retorne la lista con los elementos eliminados

```python
>>>eliminarElementosLista([254, 25, 8], [25])
[254, 8]

>>> eliminarElementosLista([54, 25, 8], [25, 54])
[8]

>>> eliminarElementosLista([54, 25, 8], [21, 24])
[54,25,8]

>>> eliminarElementosLista([], [2,4])
"Error: La primera lista debe contener al menos 1 elemento"

>>> eliminarElementosLista([23,78,9], [])
"Error: La segunda lista debe contener al menos 1 elemento"

>>> extremosLista([2,5,7,"ABC"], [2,8])
"Error: La primera lista debe elementos tipo entero"

>>> extremosLista([2,5,7], [2,"8"])
"Error: La segunda lista debe elementos tipo entero"

```
##	Niveles lista
Escriba un programa con sintaxis Python cuya función principal se llame **nivelesLista(lista)**, que reciba como entrada una lista con cualquier tipo de valores y que retorne una lista con los niveles de profundidad. La cantidad de elementos de cada sub lista debe de ser de 1

```python
>>>nivelesLista( [ [[[[]]]], 2, [] ] )
[4 ,0, 1]
>>> nivelesLista([2], [], [[[[[[]]]]]])
[1, 1, 6]
>>> nivelesLista(25)
"Error: El parámetro de entrada debe ser una lista"
```
##	Devolver Indices
Escriba un programa con sintaxis Python cuya función principal se llame **obtenerIndicesMatriz([lista1, lista2, lista3])**, que reciba como entrada una matriz y que retorne una lista de lista con los ínidces en donde aparezca un número primo o negativo

```python
v1 = [12,  56, 7 , 11 , -8, 3] 
v2 = [-26, 2, 75 , 19 , -18, 23] 
v3 = [6, 2, 10 , 50, 90] 

>>> obtenerIndicesMatriz([v1, v2, v3])
[[2,3,4,5], [0,1,3,4,5], [1]]

>>> obtenerIndicesMatriz(25)
"Error: El parámetro de entrada debe ser una lista"
```

## diagonalInversa(matriz)
Dado una matriz **cuadrada**, devolver el vector de la diagonal, iniciando con el valor del indice 0 de la última fila, hasta el valor de la última columna de la prima fila, la matriz debe tener un número impar de filas y columnas

```python
>>>diagonalInversa([[50, 25, 89], [2, 8, 9], [57, 32, 71]])
[57, 8, 89]
>>>diagonalInversa([[50, 25, 89, 10], [2, 8, 9, 4], [57, 32, 71, 11]])
'Error: La matriz debe ser de tamaño de columnas impar'
```
## formarMatrizTriangularSuperior(tamano)
- Dado un parámetro llamado **tamano**, este determinará las dimensiones de una matriz cuadrada que este sea una triangular superior. 
- Una matriz triangular superior, es aquella que apartir de su diagonal estará compuesta por el valor de 1, y debajo de la diagonal estará lleno de ceros

```python
>>>formarMatrizTriangularSuperior(3)
[[1, 1, 1], [0, 1, 1], [0, 0, 1]]

>>>formarMatrizTriangularSuperior(5)
[[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]

