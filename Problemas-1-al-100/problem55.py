def palindromo(num):

    num_str = str(num)

    if len(num_str) % 2 == 0:

        puntoTruncar = len(num_str) // 2

        parteIzquierda = num_str[0:puntoTruncar]
        parteDerecha = num_str[puntoTruncar::]
        
        palindromo = ""

        # Se agarra la parte derecha del número, y se van agregando sus caracteres, de derecha a izquierda
        for i in range(1, len(parteDerecha) + 1, 1):

            palindromo += parteDerecha[-i]

        # Lo mismo para la parte izquierda
        for j in range(1, len(parteIzquierda) + 1, 1):

            palindromo += parteIzquierda[-j]
    else:

        puntoMedio = len(num_str) // 2
        parteIzquierda = num_str[0:puntoMedio]
        parteDerecha = num_str[(puntoMedio + 1)::]
        
        palindromo = ""

        for i in range(1, len(parteDerecha) + 1, 1):

            palindromo += parteDerecha[-i]

        palindromo += num_str[puntoMedio]

        for j in range(1, len(parteIzquierda) + 1, 1):

            palindromo += parteIzquierda[-j]

    # Verifica si el palindromo, es igual al número en sí
    return int(palindromo)

def main():

    l = 1
    conteo = 0 # Conteo de Números

    while l < 10000:

        iteraciones = 0
        n = l # Número Inicial
        while True:

            suma = n + palindromo(n)
            iteraciones += 1

            if suma == palindromo(suma):

                break
            # El número es considerado Lychrel si se han hecho 50 iteraciones, y todavía no ha formado un palíndromo
            elif iteraciones == 50:

                conteo += 1
                break
            else:

                n = suma

        l += 1

    print(conteo)

main()