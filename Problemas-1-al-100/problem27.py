def ecuacionCuadratica(a, b, n):

    return n ** 2 + (a * n) + b

def esPrimo(n):

    for d in range(2, n, 1):

        if n % d == 0:

            return False

    return True

def main():

    maxCantidad = 0
    respuesta = 0

    for a in range(-999, 1000, 1):

        for b in range(-1000, 1000, 1):

            cant = 0 # Cantidad de primos que genera la ecuación cuadrática
            
            producto = a * b

            n = 0

            while True:

                r = ecuacionCuadratica(a, b, n)

                # Nota: Los primos no puede ser negativos
                if esPrimo(r) and r > 1:

                    # Si el número generado es primo, se aumenta 1 al valor de 'n'
                    cant += 1
                    n += 1
                else:

                    # Esto continúa hasta que se encuentra un valor que no es primo
                    break

            if cant > maxCantidad:

                maxCantidad = cant
                respuesta = producto # La respuesta debe ser el producto de 'a' y 'b' que genera la mayor cantidad de primos

    print(respuesta)
    print(f"{maxCantidad} primos generados en total")

main()