def main():

    resultado = 1
    
    parteDecimal = ""
    conteo = 1

    while conteo < 1000001:

        parteDecimal += str(conteo)

        conteo += 1

    multiplo10 = 1

    while multiplo10 <= 1000000:

        resultado *= int(parteDecimal[multiplo10 - 1])

        multiplo10 *= 10

    print(resultado)

main()