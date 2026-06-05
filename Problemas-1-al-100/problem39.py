from math import sqrt

def main():

    a = 1
    b = 1
    maximo = 0
    num = 0

    # Empezamos con '3'
    p = 3

    while p <= 1000:

        conteo = 0
        
        while b < p:

            # La hipotenusa se calcula automáticamente con los dos catetos
            c = sqrt(a ** 2 + b ** 2)

            if c % 1.0 == 0.0 and a + b + c == p:

                conteo += 1

            if a == p:

                b += 1
                a = b
            else:

                a += 1

        if conteo > maximo:

            num = p
            maximo = conteo

        p += 1

        a = 1
        b = 1

    print(f"{num} ({maximo})")

main()