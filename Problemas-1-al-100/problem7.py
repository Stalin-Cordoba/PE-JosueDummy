numero = 2

    conteo = 0

    while conteo < 10001:

        esPrimo = True
        for divisor in range(2, numero, 1):

            if numero % divisor == 0:

                esPrimo = False
                break

        if esPrimo:

            print(numero)
            conteo += 1

        numero += 1