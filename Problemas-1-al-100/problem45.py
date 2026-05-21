from math import sqrt

def main():

    termino = 44

    while True:

        numTriangular = (termino * (termino + 1)) // 2

        if esNumeroPentagonal(numTriangular) and esNumeroHexagonal(numTriangular):

            print(numTriangular)
        elif numTriangular > 10000:

            break
        print(numTriangular)
        termino += 1

def esNumeroPentagonal(n):

    p = (-1 - sqrt(1 + (12 * 2 * n))) / -6
    return p % 1.0 == 0.0

def esNumeroHexagonal(n):

    h = (-1 - sqrt(1 + (8 * n))) / -4
    return h % 1.0 == 0.0

main()