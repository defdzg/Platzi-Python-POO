"""
    BÚSQUEDA BINARIA
Divide y conquista. El problema se divide en 2 en cada iteración.
El algoritmo considera que la lista está órdenada.

"""

import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'Buscando el {objetivo} entre {lista[comienzo]}, {lista[final-1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que nunero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, tamano_de_lista, objetivo) #Signature

    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')