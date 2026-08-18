def factoresPrimos(numero):

    factos = []

    i = 0
    divisor = 2

    while numero != 1:

        if numero % divisor == 0:

            numero = numero // divisor
            
            # Si la lista está vacía, entonces agregamos el primer elemento
            if factos == []:

                factos.append(divisor)
            # Como sólo queremos los factores primos únicos, no incluimos cualquier factor repetido
            elif factos[i] != divisor:
                
                factos.append(divisor)
                i += 1
        else:

            divisor += 1

    return factos

# Se retoma la función Phi del ejercicio 69
def funcionPhi(num):

    valor = num
    factPrimos = factoresPrimos(num)

    for p in factPrimos:

        valor *= (1 - (1 / p))

    return int(valor)

def main():

    respuesta = 0

    for d in range(2, 1000001, 1):

        respuesta += funcionPhi(d)

    print(respuesta)

main()