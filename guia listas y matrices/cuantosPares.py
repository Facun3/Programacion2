
"""
    Guia de listas y matrices.
    Alumno: Facundo Emiliano Choque Silberman
    Profesor: Matías Bordone
    Año lectivo: ITSC 2020
"""
lista=[1,2,3,4,5,6,7,8,9,10]
lista2=[1,1,2,2,3,3,4,4,5,5]
vector1=[1,2,3]
vector2=[-1,0,2]

def cuantosPares(lista):
    i=0
    for element in lista:
        if element%2==0:
            i=i+1
    return i
print("Numero de pares:", cuantosPares(lista))


def sumaLista(lista):
    total=0
    for element in lista:
        total=total+element
    return total
print("La suma da:",sumaLista(lista))


def multiplicaLista(lista):
    total=1
    for element in lista:
        total=total*element
    return total
print("La multiplicacion da:",multiplicaLista(lista))

def maximoEnLista(lista):
    max=0
    for element in lista:
        if element>max:
            max=element
    return max
print("Maximo en la lista:",maximoEnLista(lista))

def filtrarPalabrasn(lista,n):
    return lista[:n]
print(filtrarPalabrasn(lista,4))

def multiplicarVectores(vec1,vec2):
    suma=0
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
            suma=suma+vec1[i]*vec2[i]
    return suma

print(multiplicarVectores(vector1,vector2))

def eliminaDuplicados(lista):
    return set(lista)
print(eliminaDuplicados(lista2))

