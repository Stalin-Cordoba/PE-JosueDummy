def main():

    domingos = 0
    
    anio = 1901
    diasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    diaInicial = 'Martes' # 1901 empezó un martes
    conteo = 1

    while anio < 2001:

        esBisiesto = False
        esSigloBisiesto = False
        
        if anio % 400 == 0:

            esSigloBisiesto = True

        elif anio % 4 == 0:

            esBisiesto = True
        
        if esBisiesto or esSigloBisiesto:

            diasMeses[1] += 1

        for mes in diasMeses:

            diaInicial = dias[conteo]
            if diaInicial == 'Domingo':

                domingos += 1

            diasRestantes = mes

            while diasRestantes > 1:

                if conteo == 6:

                    conteo = 0
                else:

                    conteo += 1

                diasRestantes -= 1

            diaInicial = dias[conteo]

            if conteo == 6:

                conteo = 0
            else:

                conteo += 1
        
        anio += 1

        if esBisiesto or esSigloBisiesto:

            diasMeses[1] -= 1 
    print(domingos)

main()