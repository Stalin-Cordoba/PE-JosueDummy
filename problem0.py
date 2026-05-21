def main():

    total = 0
    cuenta = 1

    while cuenta < 974001:

        cuadrado = cuenta ** 2
        if cuadrado % 2 != 0:
            
            total += cuadrado
        
        cuenta += 1

    print(total)

main()