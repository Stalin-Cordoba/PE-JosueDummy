from math import sqrt

def generarPrimos():
    
    # Agregamos el 2
    numerosPrimos = [2]

    # Para ahorrar tiempo, sólo se listan los números impares (excepto el 1)
    for i in range(3, 1000001, 2):

        numerosPrimos.append(i)
    ultimoNumero = numerosPrimos[-1]

    # Como no están los pares, excluimos el dos para el ciclo 'for'
    for divisor in numerosPrimos[1::]:

        if divisor >= sqrt(ultimoNumero):

            break
        else:
            for num in numerosPrimos:

                # Revisa todos los múltiplos de cada número en la lista
                if num % divisor == 0 and num != divisor:

                    del numerosPrimos[numerosPrimos.index(num)]

    return numerosPrimos

def rotarNumero(numero):

    n = numero
    combinaciones = []

    divisor = 1

    # Se determina primero cuántos dígitos tiene el número
    while True:

        if n // divisor >= 10:

            divisor *= 10
        else:

            break

    digitos = []
    
    while divisor > 0:

        d = n // divisor

        digitos.append(d)

        n = n - (d * divisor)

        divisor = divisor // 10

    rotaciones = [digitos]

    for r in range(0, len(digitos) - 1, 1):

        lista = rotaciones[r].copy()

        lista.insert(0, lista[-1])
        lista.pop()

        rotaciones.append(lista)

    # Si el número tiene todos sus dígitos iguales, entonces se vuelve sólo a él
    if all(r == digitos for r in rotaciones):

        return [numero]

    cant_digitos = len(rotaciones)

    for r in rotaciones:

        acumulador = 10 ** (cant_digitos - 1)
        combinacion = 0

        for d in r:

            combinacion += (d * acumulador)

            acumulador = acumulador // 10

        combinaciones.append(combinacion)

    return combinaciones

def main():

    primos = generarPrimos() # Primero, generamos los primos menores que un millón

    respuesta = len(primos)

    for p in primos:

        test = rotarNumero(p)

        for rotacion in test:

            try:

                primos.index(rotacion)
            except ValueError:

                respuesta -= 1
                break

    print(respuesta)

main()