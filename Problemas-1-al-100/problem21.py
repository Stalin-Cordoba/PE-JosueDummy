def sumaDivisores(numero):

    suma = 0

    for d in range(1, numero, 1):

        if numero % d == 0:

            suma += d

    return suma

def main():
    
    amigosSuma = 0

    sumaTotales = []
    
    for i in range(1, 10000, 1):

        sumaTotales.append(sumaDivisores(i))

    p = 220
    q = 284

    while p < 10000:

        while q < 10000:

            if sumaTotales[p - 1] == q and sumaTotales[q - 1] == p:

                amigosSuma += p
                amigosSuma += q

            q += 1

        p += 1
        q = p + 1

    print(amigosSuma)

main()