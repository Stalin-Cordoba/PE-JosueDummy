def main():

    sumaCuadrados = 0
    cuadradoSuma = 0

    n = 1

    while n < 101:

        sumaCuadrados += (n ** 2)
        cuadradoSuma += n

        n += 1

    cuadradoSuma = (cuadradoSuma ** 2)

    print(cuadradoSuma - sumaCuadrados)

main()