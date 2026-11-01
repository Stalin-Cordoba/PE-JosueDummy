def main():

    respuesta = 0

    # Los términos para la fracción continua
    lista_numeros = [2]

    for k in range(1, 34, 1):

        lista_numeros.append(1)
        lista_numeros.append(2 * k)
        lista_numeros.append(1)

        k += 1

    cant = len(lista_numeros)

    # Dado que en los términos para la fracción continua, el último número es un 1, entonces se suma con el
    # penúltimo término, para así formar la fracción a sumar continuamente
    fraccion = [1, lista_numeros[-2] + lista_numeros[-1]]

    for i in range(cant - 3, 0, -1):

        num = lista_numeros[i]

        # Se hace la suma de fraccion con el respectivo término
        fraccion[0] += (num * fraccion[1])

        # Este intercambio, es equivalente al dividir 1 entre nuestra fracción
        copia = fraccion[0]

        fraccion[0] = fraccion[1]
        fraccion[1] = copia

    # Al final, la fracción final se termina sumando por 2
    fraccion[0] += (lista_numeros[0] * fraccion[1])

    print(fraccion)

    # Se suma cada dígito del numerador
    for digito in str(fraccion[0]):

        respuesta += int(digito)
    
    print(respuesta)

main()