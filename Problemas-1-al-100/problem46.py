def esCompuesto(num):

    for d in range(2, num, 1):

        if num % d == 0:

            return True
        
    return False

def main():

    num = 1

    while True:

        esGanador = False
        if esCompuesto(num) and num % 2 != 0:

            a = 1

            while True:

                testeo = num
                testeo -= (2) * (a ** 2)

                if testeo < 0:

                    esGanador = True
                    break
                elif not esCompuesto(testeo):

                    break
                else:

                    a += 1

            if esGanador:

                print(f"El que derrota la conjetura: {num}")
                break
        
        num += 1

main()