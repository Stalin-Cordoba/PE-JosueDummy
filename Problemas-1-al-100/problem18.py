def main():

    triangulo_texto = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    triangulo = [] # El mismo triangulo, pero en una lista
    
    for fila in triangulo_texto.split('\n'):

        triangulo.append(fila.split(' '))

    for f in range(0, len(triangulo), 1):

        fila = triangulo[f]
        
        for n in range(0, len(fila), 1):

            triangulo[f][n] = int(triangulo[f][n])

    # Este arreglo muestra las posibles rutas a tomar
    ruta = []

    for i in range(0, len(triangulo), 1):

        ruta.append(list())

    # Se agrega el primer elemento de la pirámide
    ruta[0].append(triangulo[0][0])

    # Posteriormente, para los siguientes dos elementos de la 2da fila, se les suma el elemento que tienen por encima de ellos
    ruta[1].append(ruta[0][0] + triangulo[1][0])
    ruta[1].append(ruta[0][0] + triangulo[1][1])

    j = 2 # Fila actual

    while j < 15:

        i = 0 # Número en la fila

        while i <= j: # Recorre toda la fila (Número de la fila = Cantidad de elementos en esa fila)

            suma = triangulo[j][i] # Se agarra el elemento correspondiente al triangulo
            
            # Se calculan los índices de los dos números adyacentes arriba
            i_izquierdo = i - 1
            i_derecho = i

            # Si no tiene elemento a la izquierda, sólo se suma el que está a la derecha
            if i_izquierdo == -1:

                suma += ruta[j - 1][0]
            # Si no tiene elemento a la derecha, sólo se suma el que está a la izquierda
            elif i_derecho == j:

                suma += ruta[j - 1][j - 1]
            # Si tiene dos elementos a la izquierda y a la derecha, se elige el mayor
            else:

                if ruta[j - 1][i_izquierdo] > ruta[j - 1][i_derecho]:
                
                    suma += ruta[j - 1][i_izquierdo]
                else:
                
                    suma += ruta[j - 1][i_derecho]

            # Se agrega la suma realiza en nuestra lista
            ruta[j].append(suma)
            
            i += 1

        j += 1

    # Para la respuesta, imprimimos el mayor valor que está en la última fila
    print(max(ruta[-1]))

main()