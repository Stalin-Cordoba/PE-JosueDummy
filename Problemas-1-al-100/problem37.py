def truncarPrimo(p):

    valores = []
    str_primo = str(p) # Volvemos el número primo en texto

    cant_digi = len(str_primo)

    # Truncamiento a la izquierda

    for i in range(1, cant_digi, 1):

        valores.append(int(str_primo[i:cant_digi]))

    # Truncamiento a la derecha

    for j in range(cant_digi - 1, 0, -1):

        valores.append(int(str_primo[0:j]))

    return valores

def esPrimo(num):

    # NOTA: En la función 'main' dado que 'num' aumenta de 2 en 2, entonces el valor inicial a dividir es 3
    for i in range(3, (num // 2) + 1, 2):

        if num % i == 0:

            return False

    return True

def main():
    
    lista_primos = [2, 3, 5, 7]

    primos_truncables = []
    conteo = 0

    num = 11

    # Sólo hay 11 primos truncables
    while conteo != 11:
        
        if esPrimo(num):

            # Si el número es primo, entonces se agrega a la lista de primos
            # Sin embargo, todavía queda corroborar si es truncable a la izquierda y a la derecha
            lista_primos.append(num)
            
            combinaciones = truncarPrimo(num)
            esPrimoTruncable = True

            for valor in combinaciones:

                try:

                    lista_primos.index(valor)
                except ValueError:

                    # Si la combinación no se encuentra en la lista de primos, entonces no es un primo truncable
                    esPrimoTruncable = False
                    break

            # Si todas las combinaciones se encuentra en la lista de primos, entonces sí es un primo truncable
            if esPrimoTruncable:
            
                primos_truncables.append(num)
                conteo += 1
        
        num += 2 # Se le suma 2, porque todo número par (excepto el 2) no es primo

    print(primos_truncables)
    print(f"Suma total: {sum(primos_truncables)}")

main()