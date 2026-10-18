from math import log10, trunc

# La función sólo devuelve la cantidad de números que hay en la lista
def unicos(lista):

    # Ordenamos la lista original
    listaOrdenada = sorted(lista.copy())

    unicos = [listaOrdenada[0]]

    # Empezamos desde el segundo elemento
    for i in range(1, len(listaOrdenada), 1):

        # Para validar si el número no es repetido, se verifica si el anterior no es igual que él
        if listaOrdenada[i] != listaOrdenada[i - 1]:

            unicos.append(listaOrdenada[i])

    return unicos

def esPandigital(digitos):

    lista_digitos = []

    for r in range(0, len(digitos), 1):

        # Nota: El número NO puede llevar cero
        if int(digitos[r]) == 0:

            return False
        else:
            
            lista_digitos.append(int(digitos[r]))

    # Para contar los dígitos únicos de la concatenación, se ordena la lista de menor a mayor
    lista_digitos = sorted(lista_digitos.copy())

    # Si no tiene 9 dígitos exacto, no nos sirve esa combinación
    if len(lista_digitos) != 9:

        return False
    else:
    
        for j in range(1, len(lista_digitos), 1):

            # Si hay un dígito repetido, entonces no nos sirve la combinación
            if lista_digitos[j] == lista_digitos[j - 1]:

                return False

    # Si de las 3 condiciones, ninguna se cumple, entonces la combinación es factible para nuestra respuesta
    return True

def main():

    combinaciones = []

    a = 1

    # Si a = 100, entonces al multiplicar a por b, sería 100 * 100 = 10000 (hay 11 dígitos en total)
    # Por ende, no nos conviene seguir a partir de 100
    while a < 100:

        # 'b' empieza tomando el valor de 'a' para emprezar
        b = a

        while True:

            producto = a * b

            # Calcula la cantidad de dígitos que tiene  'a', 'b' y el producto entre ellos
            cant_digitos_mu = (trunc(log10(a)) + 1) + (trunc(log10(b)) + 1) + (trunc(log10(producto)) + 1)

            # Si la cantidad de dígitos en total excede de 10, se elige otro valor para 'a'
            if cant_digitos_mu >= 10:

                break
            else:

                # Concatenamos los tres números
                concatenacion = ""

                concatenacion += str(a)
                concatenacion += str(b)
                concatenacion += str(producto)

                # Si la concatenación termina siendo un número pandigital del 1 al 9, entonces lo agregamos
                if esPandigital(concatenacion):

                    combinaciones.append(producto)
                
                b += 1
        
        a += 1
    
    # Se imprimen los únicos, porque hay productos que se pueden expresar más de una manera
    print(unicos(combinaciones))
    print(f"Suma total: {sum(unicos(combinaciones))}")

main()