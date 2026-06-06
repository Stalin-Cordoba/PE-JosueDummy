def factPrimosUnicos(numero):

    factPrimos = []
    
    n = numero
    divisor = 2

    while n != 1:

        if n % divisor == 0:

            n = n // divisor
            factPrimos.append(divisor)
        else:

            divisor += 1

    factPrimos.sort()
    FPs_unicos = []

    for i in range(0, len(factPrimos), 1):

        if factPrimos[i] != factPrimos[i - 1]:

            FPs_unicos.append(factPrimos[i])

    return len(FPs_unicos)

def main():
    
    n1 = 1
    n2 = n1 + 1
    n3 = n2 + 1
    n4 = n3 + 1

    # Requerido
    r = 4

    while True:

        # Variables booleanas, para verificar si tiene 4 factores primos únicos
        corr_n1 = factPrimosUnicos(n1) == r
        corr_n2 = factPrimosUnicos(n2) == r
        corr_n3 = factPrimosUnicos(n3) == r
        corr_n4 = factPrimosUnicos(n4) == r

        if corr_n1 and corr_n2 and corr_n3 and corr_n4:

            # Sólo nos pide el primer número de los cuatro
            print(n1)
            break

        n1 += 1
        n2 += 1
        n3 += 1
        n4 += 1
        
main()