def fact(num):

    producto = 1

    for i in range(num, 0, -1):

        producto *= i

    return producto

def esPrimo(n):

    for d in range(2, n, 1):

        if n % d == 0:

            return False

    return True

def main():
    
    for valor in range(9, -1, -1):
    
        n_esimo = valor
    
        combinaciones = []

        digitos_utilizar = [] # Los dígitos que se van a utilizar

        for a in range(1, n_esimo + 1, 1):

            digitos_utilizar.append(a)

        # Se calcula cada combinación
        for v in range(1, fact(n_esimo) + 1, 1):

            respuesta = ""
        
            digitos = digitos_utilizar.copy()
        
            objetivo = v # El valor actual
            suma = 0
    
            for n in range(n_esimo - 1, -1, -1):

                i = 0
                while True:

                    # Para el i-esimo dígito, se calculan las combinaciones totales para el resto de espacios sin dígitos
                    # Si la suma no llega al objetivo establecido, se sigue con el siguiente dígito
                    suma += fact(n)

                    if suma >= objetivo:

                        suma -= fact(n)
                        break
                    else:

                        i += 1

                respuesta += str(digitos[i])
                digitos.pop(i) # Una vez utilizado un dígito, se quita del arreglo

            combinaciones.append(respuesta)

        primoPandigital = False # Existe el primo pandigital?

        # Busca primero desde los valores más grandes, hasta los menores (Porque nos están pidiendo el mayor)
        for i in range(fact(n_esimo) - 1, -1, -1):

            num = combinaciones[i]

            if esPrimo(int(num)):

                primoPandigital = True
                print(num)
                break

        # Si no hay ningún primo pandigital de 'n' dígito, entonces se vuelve a intentar con otro valor para 'n'
        if not primoPandigital:

            n_esimo -= 1 # Se reduce 'n' por 1
            combinaciones = [] # Se vacían las combinaciones
        else:

            break

main()