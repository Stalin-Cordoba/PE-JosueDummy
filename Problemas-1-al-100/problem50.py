from math import sqrt

def main():
    
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

    mayorCantNumeros = 0
    respuesta = 0
    for primo in numerosPrimos:

        for q in range(2, len(numerosPrimos), 1):

            # Va creando un rango poco a poco más grande
            # Hasta que la suma de ese rango sea igual, o mayor que el primo en particular
            listaConsecutiva = numerosPrimos[0:q]
            if primo == sum(listaConsecutiva):

                if len(numerosPrimos[0:q]) > mayorCantNumeros:

                    mayorCantNumeros = len(numerosPrimos[0:q])
                    respuesta = primo
                break
            elif sum(listaConsecutiva) > primo:

                # Si la suma es mayor, entonces se va eliminando de poco en poco los primeros términos
                # Si llega un punto donde la suma queda igual que el número primo, entonces lo tomamos en cuenta para determinar la respuesta
                # Si no, entonces significa que ese número primo no puede ser expresado como suma de primos consecutivos
                total = sum(listaConsecutiva)
                p = 1
                for num in listaConsecutiva:

                    total -= num

                    if total < primo:

                        break
                    elif total == primo:

                        if len(numerosPrimos[p:q]) > mayorCantNumeros:

                            mayorCantNumeros = len(numerosPrimos[p:q])
                            respuesta = primo
                        break
                    
                    p += 1

                break
    
    print(f"{respuesta} ({mayorCantNumeros})")

main()