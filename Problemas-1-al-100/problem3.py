def main():
    
    numero = 600851475143
    i = 2

    while i <= numero:

        if numero % i == 0:

            factorPrimo = i
            numero = numero / i
            print(numero)
        else:

            i += 1

    print(factorPrimo)

main()