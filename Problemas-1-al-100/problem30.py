def main():

    numero = 2
    resultado = 0

    while numero < 10000000:

        suma = 0
        numero_texto = str(numero)

        for s in numero_texto:

            suma += (int(s)) ** 5
        
        if suma == numero:

            resultado += numero

        numero += 1

    print(resultado)

main()