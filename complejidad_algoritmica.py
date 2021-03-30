"""
    CRECIMIENTO ASINTÓTICO

El enfoqure se centra en lo que pasa conforme el tamaño
del problema se acerca al infinito.

Big O

    EJEMPLO

# Ley de la suma

def f(n):
    for i in range(n):
        print(n)

    for i in range(n):
        print(i)

O(n) + O(n) = O(n + n) = O(2n) = O(n)
# Sólo interesa el término de mayor exponente
# La función crece en O de n

#####################

O(1) -> Constante
O(n) -> Lineal
O(log n) -> Logarítmico
O(n log n) -> log lineal
O(n**2) -> Polinomial
O(2**n) -> Exponencial

"""