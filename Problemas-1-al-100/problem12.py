def combinacion(factos, num_elegidos):

    comb = 1

    # Para encontrar la combinación, se usa un contador binario
    for j in range(0, len(factos), 1):

        # Si hay un '0', entonces se multiplica. Si no, no se multiplica
        if num_elegidos[j] == 0:

            comb *= factos[j]

    return comb

# La función sólo devuelve la cantidad de números que hay en la lista
def unicos(lista):

    # Ordenamos la lista original
    listaOrdenada = sorted(lista.copy())

    conteo = 1

    # Empezamos desde el segundo elemento
    for i in range(1, len(listaOrdenada), 1):

        # Para validar si el número no es repetido, se verifica si el anterior no es igual que él
        if listaOrdenada[i] != listaOrdenada[i - 1]:

            conteo += 1

    return conteo

def calcularDivisores(n):

    num = n

    if num == 1:
    
        return 1

    fact = []
    contador = [] # Contador binario

    divisor = 2

    while num != 1:

        if num % divisor == 0:

            fact.append(divisor)
            contador.append(0)
            num = num // divisor
        else:

            divisor += 1

    cant_fact = len(fact)

    # En un número, en caso de que sus factores primos no se repiten entre ellos
    # La cantidad de divisores que tiene ese número va a ser 2 elevado a la cantidad de factores primos
    if cant_fact == unicos(fact):

        return (2 ** cant_fact)

    divisores = []

    conteo = 0

    # La cantidad de dígitos del contador binario, es equivalente a la cantidad de factores primos del número
    while conteo < (2 ** cant_fact):

        # Se procede a calcular los productos posibles que se pueden hacer con los factores primos del número
        # ADVERTENCIA: No es muy recomendable hacer esto, debido a que, entre más factores primos, más tiempo
        divisores.append(combinacion(fact, contador))

        contador[-1] += 1

        b = 0

        # Revisa por dígito por dígito del contador binario, para revisar si no hay un 2
        while b < cant_fact:

            # En caso de encontrar un 2, se agrega un '1' al dígito detrás del dígito actual
            # El dígito actual se vuelve cero
            if contador[b] == 2:

                contador[b] = 0
                contador[b - 1] += 1

                # Se vuelve a realizar la búsqueda si hay otro 2
                b = 0
            else:

                b += 1

        conteo += 1

    # Se retorna los elementos únicos
    return unicos(divisores)

def main():

    n = 1

    while True:

        numeroTriangular = (n * (n + 1)) // 2
        
        if calcularDivisores(numeroTriangular) > 500:

            print(numeroTriangular)
            break
        
        n += 1

main()