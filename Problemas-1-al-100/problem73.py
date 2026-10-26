def factoresPrimosUnicos(num):

    factores = []

    divisor = 2
    n = num

    while n != 1:

        if n % divisor == 0:

            factores.append(divisor)

            n = n // divisor
        else:

            divisor += 1

    facts_unicos = [factores[0]]

    # Sólo se retorna los factores primos únicos del número
    for j in range(1, len(factores), 1):

        if factores[j] != factores[j - 1]:

            facts_unicos.append(factores[j])
    
    return facts_unicos

def determinarFracciones(lista_numeros, facts, num):

    cant = len(lista_numeros)
    
    # 'f' es Factor primo
    for f in facts:

        j = 1

        # Se van quitando todos los múltiplos del factor primo correspondiente
        while j <= (cant - 1):

            if lista_numeros[j] % f == 0:

                del lista_numeros[j]
                cant -= 1
            else:

                j += 1

    # Se adjuntan los valores que quedaron
    for n in range(0, cant, 1):

        lista_numeros[n] = lista_numeros[n] / num
    
    return lista_numeros

def main():
    
    lista_fracciones = []

    lista_numeros = [1]

    for d in range(2, 12001, 1):

        # Dado que el numerador de la fracción, tiene que ser mayor que 1, y menor que el denominador, se utiliza
        # una lista de los números precedentes para todos los valores del 'd'
        lista_numeros.append(d)

        factos = factoresPrimosUnicos(d)

        fracs_reducidas = determinarFracciones(lista_numeros.copy(), factos, d)

        # Las fracciones reducidas se adjuntan a una lista
        for f in fracs_reducidas:

            lista_fracciones.append(f)

    # La ordenamos de menor a mayor las fracciones reducidad
    lista_fracciones = sorted(lista_fracciones.copy())

    # Calculamos la cantidad de fracciones que hay entre (1/3) y (1/2)
    respuesta = (lista_fracciones.index(0.5) - lista_fracciones.index(0.3333333333333333)) - 1
    print(respuesta)

main()