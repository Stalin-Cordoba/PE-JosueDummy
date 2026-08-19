def quitarDigitos(num, den):

    valores = []

    de1 = num // 10
    u1 = num - (de1 * 10)

    de2 = den // 10
    u2 = den - (de2 * 10)

    # Verifica si el numerador y denominador tienen dígitos en común
    if de1 == de2:

        valores.append(u1 / u2)
    elif u1 == de2:

        valores.append(de1 / u2)
    elif u2 == de1:

        valores.append(u1 / de2)
    elif u1 == u2:

        valores.append(de1 / de2)
    
    return valores

def main():

    fracciones_correctas = []

    numerador = 11

    while numerador < 100:

        denominador = numerador + 1

        # El cero no puede ser incluido
        if denominador % 10 == 0:

            denominador += 1

        while denominador < 100:

            valor_fraccion = numerador / denominador

            # Aquí se obtienen los valores después de la simplificación mal hecha
            valores_obtenidos = quitarDigitos(numerador, denominador)

            for v in valores_obtenidos:

                # Si con la simplicación mal hecha, el valor coincide, entonces se incluye en una lista para la respuesta
                if valor_fraccion == v:

                    fracciones_correctas.append([numerador, denominador])
                    break

            denominador += 1
            
            # El cero no puede ser incluido
            if denominador % 10 == 0:
            
                denominador += 1

        # Para que no sea un ciclo infinito
        numerador += 1

        # El cero no puede ser incluido
        if numerador % 10 == 0:

            numerador += 1

    print(f"Fracciones elegidas para la respuesta: {fracciones_correctas}")

    num_respuesta = 1
    den_respuesta = 1

    for fr in fracciones_correctas:

        num_respuesta *= fr[0]
        den_respuesta *= fr[1]

    # El problema indica que hay que expresar la fraccion que nos da la respuesta en su expresión mínima

    divisor = 2

    while divisor < den_respuesta:

        if num_respuesta % divisor == 0 and den_respuesta % divisor == 0:

            num_respuesta //= divisor
            den_respuesta //= divisor
        else:

            divisor += 1

    print(f"\nRespuesta definitiva {den_respuesta}")

main()