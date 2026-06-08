def sumaDivisores(numero):

    suma = 0

    for d in range(1, numero, 1):

        if numero % d == 0:

            suma += d

    return suma

def main():
    
    amigosSuma = 0

    # Se calcula los totales para los números del 1 al 9999
    sumaTotales = []
    
    for i in range(1, 10000, 1):

        sumaTotales.append(sumaDivisores(i))

    p = 1
    q = p + 1

    while p < 10000:

        while q < 10000:

            # Se verifica la condición
            if sumaTotales[p - 1] == q and sumaTotales[q - 1] == p:

                amigosSuma += p
                amigosSuma += q

            q += 1

        p += 1
        q = p + 1

    print(amigosSuma)

main()