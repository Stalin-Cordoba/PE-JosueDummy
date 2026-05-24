# La función 'time' la pongo para ver que tanto me tardé en esperar la respuesta
from time import time

def test():
    
    inicio = time()
    
    listaNumeros = []

    # Para ahorrar tiempo, sólo se listan los números impares (excepto el 1)
    for i in range(3, 2000001, 2):

        listaNumeros.append(i)

    for divisor in listaNumeros:

        for num in listaNumeros:

            # Revisa todos los múltiplos de cada número en la lista
            if num % divisor == 0 and num != divisor:

                del listaNumeros[listaNumeros.index(num)]

    fin = time()
    print(sum(listaNumeros) + 2) # Cómo en la lista sólo están los impares, debemos sumar el 2 (porque es primo también)
    print(fin - inicio)

test()