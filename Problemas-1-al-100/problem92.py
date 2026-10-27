def sumarDigitosCuadrados(n):

    n_str = str(n)
    suma = 0

    # Se descompone el número, en cada uno de sus dígitos
    # Cada dígito es elevado al cuadrado y se suma
    for char in n_str:

        suma += int(char) ** 2

    return suma

def main():

    respuesta = 0
    
    numero_empezar = 1 # El número con el que se comienza

    while numero_empezar < 10000000:

        n = numero_empezar
        n_anterior = n

        while True:

            n = sumarDigitosCuadrados(n_anterior)

            # Si termina en 1, se concluye el ciclo, pero el problema no nos pide los números que terminan en 1
            if n == 1:

                break
            # Si termina en 89, se termina el ciclo
            elif n == 89:

                respuesta += 1
                break
            # Si no es ninguna de las anteriores, se continúa el ciclo
            else:

                n_anterior = n

        numero_empezar += 1

    print(respuesta)

main()