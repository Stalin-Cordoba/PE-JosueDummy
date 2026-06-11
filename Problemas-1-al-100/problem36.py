def conversionBin(numDec):

    digitos = []
    numBin = ""
    numero = numDec

    while numero != 1:

        residuo = numero % 2
        digitos.append(residuo)
        numero = numero // 2
    
    digitos.append(numero)

    for n in range(-1, -len(digitos) - 1, -1):

        numBin += str(digitos[n])

    return numBin

def esPalindromo(num):

    num_str = str(num)

    # Si es un sólo número, devolvemos 'True', porque es el número en sí
    if len(num_str) == 1:
    
        return True
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
    return palindromo == num_str

def main():

    suma = 0

    for n in range(1, 1000000, 1):

        binario = conversionBin(n)
        
        # Verifica si los dos números son palíndromos
        if esPalindromo(n) and esPalindromo(binario):

            suma += n

    print(suma)

main()