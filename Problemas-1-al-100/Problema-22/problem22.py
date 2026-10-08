def ordenar(palabra1, palabra2, dicc): # Se necesita las dos palabras y el diccionario de letras
    
    elegida = None
    
    # Cantidad de letras en las dos palabras
    cant_let1 = len(palabra1)
    cant_let2 = len(palabra2)

    if cant_let1 >= cant_let2:

        m = cant_let1
    else:

        m = cant_let2

    # Compara letra por letra, para determinar cuál de las dos palabras va primero
    for i in range(0, m, 1):

        # Estos 'try', se usan cuando una palabra actúa como un 'subtring' al inicio de la otra palabra
        try:
            lp1 = palabra1[i] # Letra actual de la primera palabra
        except IndexError:
            return palabra1
        
        try:
            lp2 = palabra2[i] # Letra actual de la segunda palabra
        except IndexError:
            return palabra2

        if dicc[lp1] > dicc[lp2]:
        
            elegida = palabra2
            break
        elif dicc[lp1] < dicc[lp2]:

            elegida = palabra1
            break

    # Si las dos palabras son iguales, entonces sólo se retorna la primer palabra
    if elegida == None:

        return palabra1
    else:

        return elegida

def calcularPuntuacion(palabra, dicc, lugar_lista):

    suma_caracteres = 0

    # Por cada carácter en la palabra
    for c in palabra:

        suma_caracteres += dicc[c]

    # Se retorna producto entre la suma de los caracteres y su posición en la lista
    return suma_caracteres * lugar_lista

def main():

    # Diccionario para las letras
    letras = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 
              'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 
              'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
    
    with open('Problemas-1-al-100/Problema-22/0022_names.txt') as lista_completa:

        lista_texto = lista_completa.read()
    
    nombres = lista_texto.split(',')
    
    cant = len(nombres)

    # Cómo en el archivo .txt, los nombres van con comillas, hay que quitarlos
    for k in range(0, cant, 1):

        nombres[k] = nombres[k].replace('"','')

    respuesta = 0

    # Nota: El algoritmo que se usa para ordenar los nombres es: Selection Sort
    for i in range(0, cant - 1, 1):

        indice_ord = i
        nombre_ord = nombres[i]

        for j in range(i + 1, cant, 1):

            comp = nombres[j]

            if ordenar(nombre_ord, comp, letras) == comp:

                indice_ord = j
                nombre_ord = comp

        nombres[indice_ord] = nombres[i]
        nombres[i] = nombre_ord

    for p in range(0, cant, 1):

        # En el último parámetro, se le suma 1 porque trabajamos con índices de lista
        respuesta += calcularPuntuacion(nombres[p], letras, p + 1)

    print(respuesta)

main()