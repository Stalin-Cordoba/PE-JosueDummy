def main():

    suma = 0

    f1 = 1
    f2 = 1

    F = f2 + f1
    print(f1)
    print(f2)
    print(F)

    while F < 4000000:

        if F % 2 == 0:
            suma += F

        copia = f2

        f2 = F
        f1 = copia

        F = f2 + f1

        print(F)

    print(f"Suma: {suma}")
main()