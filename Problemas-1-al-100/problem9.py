def main():

    a = 1
    b = 2
    c = 3

    while a < 1001:

        if a < b and b < c:

            if (a ** 2 + b ** 2) == c ** 2 and (a + b + c) == 1000:

                print(f"Tripleto: {a},{b},{c}")
                print(a * b * c)

        if c < 1000:

            c += 1
        else:

            if b < (c - 1):

                b += 1

                # 'c' toma el valor de 'b'. Se le añade 1 para cumplir que 'b < c'
                c = b + 1
            else:

                a += 1

                b = a + 1
                c = b + 1

main()