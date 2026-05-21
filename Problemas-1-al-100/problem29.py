def main():

    lista = []

    for a in range(2, 101, 1):

        for b in range(2, 101, 1):

            repetido = False
            resultado = a ** b

            # Búsqueda lineal
            for num in lista:

                if resultado == num:

                    repetido = True

            if not repetido:

                lista.append(resultado)

    print(len(lista))

main()