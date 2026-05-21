def factorial(numero):

    fact = 1
    for i in range(numero, 0, -1):

        fact *= i

    return fact

def main():

    numero = factorial(100)

    suma = 0

    for i in str(numero):

        suma += int(i)

    print(suma)

main()