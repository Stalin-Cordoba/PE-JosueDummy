from math import sqrt

# Números primos menores que 10000
def listaPrimos():

    # Agregamos el 2
    numerosPrimos = [2]

    # Para ahorrar tiempo, sólo se listan los números impares (excepto el 1)
    for i in range(3, 10001, 2):

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
    
    indice_fin = numerosPrimos.index(1487)
    del numerosPrimos[0:indice_fin] # No nos interesa los primos menores que 1487, así que los eliminamos
    return numerosPrimos

def main():

    primos = listaPrimos()
    respuestaEncontrada = False

    # No empezamos por '1487', sino que empezamos por el primo después de este
    for a1 in primos[1::]:

        d = 1
        a2 = a1 + d
        a3 = a2 + d

        if respuestaEncontrada:

            break # FIN
        else:
            while a3 < 10000: # El último término no debe que tener 5 dígitos o más

                # Verifica si los dós términos son primos
                if any(p == a2 for p in primos) and any(p == a3 for p in primos):

                    secuencia = [str(a1), str(a2), str(a3)] # Los términos de la secuencia se vuelve 'String'
                    secuencia_digitos = [] # Se almacenan las listas de los dígitos de cada término
                    
                    for termino in secuencia:

                        digitos = []

                        for digito in termino:

                            # Los dígitos que están en 'String', se vuelven Enteros
                            digitos.append(int(digito))

                        digitos = sorted(digitos) # Se ordena la lista
                        secuencia_digitos.append(digitos)

                    # Una vez que se encuentra la respuesta, se termina el programa
                    if all(sd == secuencia_digitos[0] for sd in secuencia_digitos):

                        print(f"Respuesta: {a1}{a2}{a3}") # Los tres términos se muestran pegaditos
                        respuestaEncontrada = True
                        break
            
                d += 1
                a2 = a1 + d
                a3 = a2 + d
    
main()