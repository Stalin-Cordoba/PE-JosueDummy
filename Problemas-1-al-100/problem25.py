def main():

    f1 = 1
    f2 = 1

    indice = 3 # Contamos el índice a partir del tercer término
    
    while True:

        F = f2 + f1

        if len(str(F)) >= 1000:

            print(indice)
            break
        else:

            copia = f2
        
            f2 = F
            f1 = copia

            indice += 1

main()