def main():

    a = 1
    b = 1
    mayorSuma = 0

    while a < 100:
        
        while b < 100:

            operacion = a ** b

            operacion = str(operacion) # Lo convertimos a string

            suma = 0
            for digito in operacion:

                suma += int(digito) # Sumamos cada dígito

            if suma > mayorSuma:

                mayorSuma = suma

            b += 1

        b = 1
        a += 1

    print(mayorSuma)

main()