"""
    COMPLEJIDAD ALGORÍTMICA

Nos permite comparar la eficiencia entre dos diferentes algoritmos.
Complejidad temporal y espacial.
"""

import time

def factorial(n):
    resupuesta = 1

    while n > 1:
        resupuesta *= n
        n -= 1

    return resupuesta

def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':

    n = 20000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final-comienzo)