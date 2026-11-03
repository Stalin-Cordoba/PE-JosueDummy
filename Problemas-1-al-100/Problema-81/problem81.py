def calcularRuta(tri, total_filas):

    triangulo = tri
    
    # Este arreglo muestra las posibles rutas a tomar
    ruta = []
    
    for i in range(0, total_filas, 1):
    
        ruta.append(list())
    
    # Se agrega el primer elemento de la pirámide
    ruta[0].append(triangulo[0][0])
    
    # Posteriormente, para los siguientes dos elementos de la 2da fila, se les suma el elemento que tienen por encima de ellos
    ruta[1].append(ruta[0][0] + triangulo[1][0])
    ruta[1].append(ruta[0][0] + triangulo[1][1])
    
    j = 2 # Fila actual
    
    while j < total_filas:
    
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
            # Si tiene dos elementos a la izquierda y a la derecha, se elige el menor
            else:
    
                if ruta[j - 1][i_izquierdo] <= ruta[j - 1][i_derecho]:
                    
                    suma += ruta[j - 1][i_izquierdo]
                else:
                    
                    suma += ruta[j - 1][i_derecho]
    
            # Se agrega la suma realiza en nuestra lista
            ruta[j].append(suma)
                
            i += 1
    
        j += 1

    return ruta[-1]

def main():

    with open('Problemas-1-al-100/Problema-81/0081_matrix.txt') as puroTexto:

        bruh = puroTexto.read()

    filas_planas = bruh.split('\n')

    matriz = []

    f = 0

    # Se construye la matriz
    for fila in filas_planas:

        matriz.append(list())

        for num in fila.split(','):

            matriz[f].append(int(num))

        f += 1

    cant_filas = len(matriz)

    triangulo_superior = []
    triangulo_inferior = []

    # Se saca la matriz triangular superior
    for m in range(0, cant_filas, 1):

        triangulo_superior.append(list())
        
        f = 0 # Fila
        c = m # Columna

        while f <= m:

            triangulo_superior[m].append(matriz[f][c])

            f += 1
            c -= 1

    indice_mti = 0 # Índice para construir la matriz triangular inferior

    # Se saca la matriz triangular inferior
    for x in range(cant_filas - 1, 0, -1):

        triangulo_inferior.append(list())

        f = cant_filas - 1
        c = x

        while c <= (cant_filas - 1):

            triangulo_inferior[indice_mti].append(matriz[f][c])

            f -= 1
            c += 1

        indice_mti += 1

    # NOTA: Aquí se utiliza un algoritmo que se usó para el problema 18 y 67
    cant_filas_TS = len(triangulo_superior)
    cant_filas_TI = len(triangulo_inferior)

    rutas_mts = calcularRuta(triangulo_superior, cant_filas_TS) # Las rutas para la matriz triangular superior
    
    rutas_mti = calcularRuta(triangulo_inferior, cant_filas_TI) # Las rutas para la matriz triangular inferior

    sumas = []

    # Por error mío, las rutas de la matriz triangular inferior, están al revés XD
    # No hay problema con esto, sólo podemos listar los elementos en reversa
    nueva_rutas_mti = []

    for i in range(1, len(rutas_mti) + 1, 1):

        nueva_rutas_mti.append(rutas_mti[-i])

    # Los resultados de todas las rutas de la matriz triangular inferior, se suma con dos resultados de las rutas de
    # la matriz triangular superior
    for j in range(0, len(rutas_mti), 1):

        sumas.append(nueva_rutas_mti[j] + rutas_mts[j])
        sumas.append(nueva_rutas_mti[j] + rutas_mts[j+1])

    # Se saca solamente el mínimo
    print(min(sumas))

main()