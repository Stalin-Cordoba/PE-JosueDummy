def numeroTriangular(n):

    return (n * (n + 1)) // 2

def main():

    num_filas = 20
    
    respuesta = numeroTriangular(num_filas + 1)

    lista_comb = [] # Se inserta los valores desde el valor de 'num_filas' hasta 1

    for i in range(num_filas, 0, -1):

        lista_comb.append(i)

    c = 0

    # Se usa combinaciones recursivas para calcular más rápido el resultado
    while c != (num_filas - 2):
        
        nueva_lista_c = []
        
        l = num_filas

        while l > 0:

            suma = sum(lista_comb) # Se calcula la suma de los elementos de la lista
            nueva_lista_c.append(suma) # Se inserta la suma en otra lista, la cual va a ser utilizada en la otra iteración
            lista_comb.pop(0) # Se remueve uno por uno, hasta que no quede nada

            l -= 1

        # Se calcula la suma de los elementos de la lista
        respuesta += sum(nueva_lista_c)

        # Para la siguiente iteración, se utiliza la nueva lista que hemos formado
        lista_comb = nueva_lista_c
        c += 1

    print(respuesta)

main()