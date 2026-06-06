def digitosUsados(numero):

    listaDigitos = []

    for c in range(0, 9, 1):

        # Cómo el número debe utilizar los dígitos del 1 al 9, el cero no debe ser incluido
        if int(numero[c]) != 0:
        
            listaDigitos.append(int(numero[c]))

    listaDigitos.sort()
    unicos = 1

    for i in range(1, len(listaDigitos), 1):

        if listaDigitos[i] != listaDigitos[i - 1]:

            unicos += 1

    return unicos

def main():

    maximo = 0

    num = 1
    
    # Dado que 'n' tiene que ser mayor que 1, sólo vamos del 1 al 9999
    while num < 10000:

        numeroPandigital = ""
        n = 1
        
        while len(numeroPandigital) < 9:

            producto = num * n
        
            numeroPandigital += str(producto)

            n += 1

        if len(numeroPandigital) == 9:
        
            # Verifica si los dígitos del 1 al 9 son utilizados en el número completo
            if digitosUsados(numeroPandigital) == 9:

                if int(numeroPandigital) > maximo:

                    maximo = int(numeroPandigital)
        
        num += 1

    print(maximo)

main()