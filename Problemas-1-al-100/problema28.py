def main():

    numeros = []

    for i in range(1, (1001 ** 2) + 1, 1):

        numeros.append(i)

    suma = 1 # Se suma el uno directamente
    p = 2 # Posicion en la lista
    salto = 2
    k = 1
    while p < len(numeros):

        suma += numeros[p]

        # Una vez que se haya sumado 4 veces, el salto se vuelve más grande
        if k == 4:

            salto += 2
            k = 1
        else:

            k += 1

        p += salto

    print(suma)

main()