def digitosUtilizados(numero):

    num_str = str(numero)
    listaDigitos = []

    for i in num_str:

        listaDigitos.append(int(i))

    
    return sorted(listaDigitos)

def main():

    x = 1

    while True:

        x_2 = x * 2
        x_3 = x * 3
        x_4 = x * 4
        x_5 = x * 5
        x_6 = x * 6

        digitos_x1 = digitosUtilizados(x)
        digitos_x2 = digitosUtilizados(x_2)
        digitos_x3 = digitosUtilizados(x_3)
        digitos_x4 = digitosUtilizados(x_4)
        digitos_x5 = digitosUtilizados(x_5)
        digitos_x6 = digitosUtilizados(x_6)

        cantDigitos = [digitos_x1, digitos_x2, digitos_x3, digitos_x4, digitos_x5, digitos_x6]

        if all(d == digitos_x1 for d in cantDigitos):

            print(f"{x} {x_2} {x_3} {x_4} {x_5} {x_6}")
            print(f"{digitos_x1} {digitos_x2} {digitos_x3} {digitos_x4} {digitos_x5} {digitos_x6}")
            print(f"Respuesta: {x}")
            break
        else:

            x += 1

main()