def main():

    num = 1
    mayorCadena = 1
    xd = 1
    while num < 1000001:

        longitudCadena = 1
        collatz = num
        while True:

            if collatz == 1:

                if longitudCadena > mayorCadena:

                    mayorCadena = longitudCadena
                    xd = num

                num += 1
                break
            else:

                longitudCadena += 1
                if collatz % 2 == 0:

                    collatz /= 2
                else:

                    collatz *= 3
                    collatz += 1

    print(mayorCadena)
    print(xd)

main()