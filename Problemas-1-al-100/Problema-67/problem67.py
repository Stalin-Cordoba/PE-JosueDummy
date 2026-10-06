# NOTA: Para este problema, se usa el mismo algoritmo para el problema 18

def main():

    with open('Problemas-1-al-100/Problema-67/0067_triangle.txt') as muchoTexto:

        triangulo_texto = muchoTexto.read()

    triangulo = [] # El mismo triangulo, pero en una lista
    
    for fila in triangulo_texto.split('\n'):

        triangulo.append(fila.split(' '))
    
    triangulo.pop() # Por algún motivo, se genera una lista vacía al final xdxd

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

    while j < 100:

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