from math import sqrt

# Las funciones para calcular la suma y la diferencia
# 'n' es el término correspondiente
# 'k' es la diferencia de índice que tiene con el n-ésimo término

def diferencia(n, k):

    return ((6 * n * k) + (3 * (k ** 2)) - k) // 2

def suma(n, k):

    return ((6 * (n ** 2)) - (2 * n) + (6 * n * k) + (3 * (k ** 2)) - k) // 2

def numeroPentagonal(n):

    return (3 * (n ** 2) - n) // 2

def eqCuadratica(v):

    # Verifica si el número es pentagonal. La ecuación cuadrática (simplificada) es la siguiente
    x = (1 + sqrt(1 - (4 * 3 * -2 * v))) / 6

    return x.is_integer()

def main():

    par_encontrado = False
    
    k = 1

    while True:

        k_actual = k

        # Se prueba con cada valor de 'n' (menor o igual que 'k')
        for n in range(1, k_actual + 1, 1):

            S = suma(n,k_actual)
            D = diferencia(n,k_actual)

            # Si la diferencia y la suma son números pentagonales, ahí tenemos nuestra respuesta
            if eqCuadratica(S) and eqCuadratica(D):

                print(numeroPentagonal(n))
                print(numeroPentagonal(n + k_actual))
                print(f"n:{n} k:{k_actual}")
                print(f"Suma: {S}")
                print(f"Diferencia: {D}")
                
                par_encontrado = True
                break

            # Se le resta 1 a 'k' para el siguiente valor a 'k'
            k_actual -= 1

        if not par_encontrado:
        
            k += 1
        else:

            break

main()