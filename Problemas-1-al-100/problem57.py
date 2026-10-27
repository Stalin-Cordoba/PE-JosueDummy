def main():

    respuesta = 0

    for e in range(1, 1001, 1):
        
        # Usamos una lista porque necesitamos el numerador y denominador (también para evitar error de punto flotante)
        fraccion = [1, 2]

        # La cantidad de veces que se repite este proceso es:
        # (N-ésima expresión - 1)
        for n in range(e, 1, -1):

            # Como solo estamos considerando la raíz cuadrada de 2, entonces se le suma 2 a la fracción
            fraccion[0] += (2 * fraccion[1])

            # Este intercambio, es equivalente al dividir 1 entre nuestra fracción
            copia = fraccion[0]

            fraccion[0] = fraccion[1]
            fraccion[1] = copia

        fraccion[0] += (1 * fraccion[1])

        # Calculamos la cantidad de dígitos en el numerador y denominador
        digitos_num = len(str(fraccion[0]))
        digitos_den = len(str(fraccion[1]))
        
        # Si la cantidad de dígitos
        if digitos_num > digitos_den:

            respuesta += 1

    print(respuesta)

main()