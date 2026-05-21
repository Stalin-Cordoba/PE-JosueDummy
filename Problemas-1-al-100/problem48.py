def main():

    print("Problema 48")

    x = 1
    suma = 0

    while x < 1001:

        suma += (x ** x)

        x += 1
    
    suma = str(suma)
    print(suma)

main()