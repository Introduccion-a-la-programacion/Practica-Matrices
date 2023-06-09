import Matrices;
import pytest;

p = Matrices
    
#####################################################################################################

def test_extremosLista_1():
    assert p.extremosLista([18,5,8,45,96, 60]) == [5,96]

def test_extremosLista_2():
    assert p.extremosLista([96, 96,96]) == [96]

def test_extremosLista_3():
    assert isinstance(p.extremosLista([]), str) == isinstance("Error: La lista debe contener al menos 2 elementos", str)

def test_extremosLista_4():
    assert isinstance(p.extremosLista([2,5,7,"ABC"]), str) == isinstance("Error: La lista debe contener elementos tipo entero", str)
    
#####################################################################################################

def test_eliminarElementosLista_1():
    assert p.eliminarElementosLista([254, 25, 8], [25]) == [254, 8]

def test_eliminarElementosLista_2():
    assert p.eliminarElementosLista([54, 25, 8], [25, 54]) == [8]

def test_eliminarElementosLista_3():
    assert p.eliminarElementosLista([54, 25, 8], [21, 24]) == [54,25,8]

def test_eliminarElementosLista_4():
    assert isinstance(p.eliminarElementosLista([], [2,4]), str) == isinstance("Error: La primera lista debe contener al menos 1 elemento", str) 

def test_eliminarElementosLista_5():
    assert isinstance(p.eliminarElementosLista([23,78,9], []), str) == isinstance("Error: La segunda lista debe contener al menos 1 elemento", str) 

def test_eliminarElementosLista_6():
    assert isinstance(p.extremosLista([2,5,7,"ABC"], [2,8]), str) == isinstance("Error: La primera lista debe elementos tipo entero", str) 

def test_eliminarElementosLista_7():
    assert isinstance(p.extremosLista([2,5,7], [2,"8"]), str) == isinstance("Error: La segunda lista debe elementos tipo entero", str) 

#####################################################################################################

def test_nivelesLista_1():
    assert p.nivelesLista([ [[[[]]]], 2, [] ] ) == [4 ,0, 1]
def test_nivelesLista_2():
    assert p.nivelesLista([ [2], [], [[[[[[]]]]]] ]) == [1, 1, 6]
def test_nivelesLista_3():
    assert isinstance(p.nivelesLista(25), str) == isinstance("Error: El parámetro de entrada debe ser una lista", str) 
    
#####################################################################################################

v1 = [12,  56, 7 , 11 , -8, 3] 
v2 = [-26, 2, 75 , 19 , -18, 23] 
v3 = [6, 2, 10 , 50, 90] 

def test_obtenerIndicesListas_1():
    assert p.obtenerIndicesMatriz([v1, v2, v3]) == [[2,3,4,5], [0,1,3,4,5], [1]]

def test_obtenerIndicesListas_2():
    assert isinstance(p.obtenerIndicesMatriz(25), str) == isinstance("Error: El parámetro de entrada debe ser una lista", str)
    
#########################################################################    
    
def test_diagonalInversa_1():
    assert p.diagonalInversa([[50, 25, 89], [2, 8, 9], [57, 32, 71]]) == [57, 8, 89]
    
def test_diagonalInversa_2():
    assert isinstance(str(p.diagonalInversa([[50, 25, 89, 10], [2, 8, 9, 4], [57, 32, 71, 11]])), str) == isinstance('Error: La matriz debe ser de tamaño de columnas impar',str)
    
#########################################################################    
    
def test_formarMatrizTriangularSuperior_1():
    assert p.formarMatrizTriangularSuperior(3) ==  [[1, 1, 1], [0, 1, 1], [0, 0, 1]]

def test_formarMatrizTriangularSuperior_2():
    assert p.formarMatrizTriangularSuperior(5) == [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]   
    

#########################################################################        
    
    
miMatriz = [ [0,0,0,0,0], [0,1,3,2,0], [0,1,3,2,0], [0,1,3,2,0],  [0,0,0,0,0]]
miMatriz2 = [ [0,0,0,0,0], [8,1,3,2,0], [0,1,3,2,0], [0,1,3,2,0],  [0,0,0,0,0]]

def test_bordesDeMatriz_1():
    assert p.bordesDeMatriz(miMatriz) == True
    
def test_bordesDeMatriz_2():
    assert p.bordesDeMatriz(miMatriz2) == False
    
#########################################################################         

matriz1 = [ [1,2,0,4,5], [1,0,0,0,5], [0,0,0,0,0],[ 1,0,0,0,5], [1,2,0,4,5]]
matriz2 = [ [1,2,0,4,5], [1,0,0,0,5], [0,0,5,0,0],[ 1,0,0,0,5], [1,2,0,4,5]]

def test_matrizDiamante_1():
    assert p.matrizDiamante(matriz1) == True
    
def test_matrizDiamante_2():
    assert p.matrizDiamante(matriz1) == False    
