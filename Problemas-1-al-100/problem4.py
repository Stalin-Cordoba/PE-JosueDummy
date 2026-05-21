def main():

    numero1 = 100
    numero2 = 100
    palindromoMayor = 0

    while numero2 < 1000:

        esPalindromo = False
        
        pro = numero1 * numero2 # Producto entre los dos números
        pro = str(pro)
        chars = len(pro)

        if chars % 2 == 0:

            initSub = pro[(chars // 2):]
            subtring = ""
            for c in range(len(initSub) - 1, -1, -1):

                subtring += initSub[c]

            if pro[0:(chars//2)] == subtring:

                esPalindromo = True
                print(pro)
        else:

            initSub = pro[(chars // 2) + 1:]
            subtring = ""
            for c in range(len(initSub) - 1, -1, -1):

                subtring += initSub[c]

            if pro[0:(chars//2)] == subtring:

                esPalindromo = True
                print(pro)
        
        if esPalindromo and (numero1 * numero2) > palindromoMayor:

            palindromoMayor = numero1 * numero2
        
        if numero1 < 1000:

            numero1 += 1
        else:

            numero1 = 100
            numero2 += 1

    print(palindromoMayor)

main()