# 2021 Semestre 2
# Portafolio 2 Parte B

## Instrucciones Generales
- El archivo **debe** llamarse **Portafolio2B.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación **Recursiva de COLA**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Fecha de entrega: **Miércoles 6 de Ovtubre a las 10pm**

##	Invertir elementos lista
Escriba un programa con sintaxis Python cuya función principal se llame **invertirLista(lista)**, que reciba como entrada una lista con números enteros denominado **lista** y que retorne la lista pero con los elementos invertidos 


```python
>>>invertirLista([5,8,45,96])
[96, 45, 8, 5]

>>> invertirLista([56, 85,8,45,96])
[96, 45, 8, 85, 56]

>>> invertirLista([])
"Error: La lista debe contener al menos 2 elementos"

>>> invertirLista([2,5,7,"ABC"])
"Error: La lista debe elementos tipo entero"
```

##	Elemento menor y mayor de la lista
Escriba un programa con sintaxis Python cuya función principal se llame **extremosLista(lista)**, que reciba como entrada una lista con números enteros denominado **lista** y que retorne la lista con 2 elementos donde ellos serán el número menor y mayor de la lista

```python
>>>extremosLista([18,5,8,45,96, 60])
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
Escriba un programa con sintaxis Python cuya función principal se llame **obtenerIndicesListas([lista1, lista2, lista3])**, que reciba como entrada una lista con lista y que retorne una lista de lista con los ínidces en donde aparezca un número primo o negativo

```python
v1 = [12,  56, 7 , 11 , -8, 3] 
v2 = [-26, 2, 75 , 19 , -18, 23] 
v3 = [6, 2, 10 , 50, 90] 

>>> obtenerIndicesListas([v1, v2, v3])
[[2,3,4,5], [0,1,3,4,5], [1]]

>>> obtenerIndicesListas(25)
"Error: El parámetro de entrada debe ser una lista"

```
