def factorial(numero):

    fact = 1

    for i in range(numero, 0, -1):

        fact *= i

    return fact


def main():

    n = 1
    r = 1
    resultado = 0

    while n <= 100:

        while r <= n:

            combinaciones = (factorial(n)) // ((factorial(r)) * (factorial(n - r)))

            if combinaciones > 1000000:

                resultado += 1

            r += 1
        
        n += 1
        r = 1

    print(resultado)

main()