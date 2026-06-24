def factoresPrimos(numero):

    # Directamente, se incluye el '2', porque sólo estamos usando los números pares
    factos = [2]

    i = 0

    n = numero // 2
    divisor = 2

    while n != 1:

        if n % divisor == 0:

            n = n // divisor
            
            # Como sólo queremos los factores primos únicos, no incluimos cualquier factor repetido
            if factos[i] != divisor:
                
                factos.append(divisor)
                i += 1
        else:

            divisor += 1

    return factos

def funcionPhi(num):

    primos = factoresPrimos(num) # Factores primos únicos
    cant_primos = len(primos)

    inicio = 0
    fin = 0
    
    # Se almacenan todos los posibles productos que se pueden formar, elegiendo cierta cantidad de factores primos
    total = []
    
    # Esta lista guarda todos los conjuntos formados cuando se multiplican tal cantidad de factores primos
    lista_conjuntos = [primos]

    # Guarda las listas creadas a partir de 'fusiones' (Mire la línea 83)
    lista_fusiones = []

    if cant_primos == 1:

        # Si sólo se usa un sólo factor primo, entonces se divide 'n' (restandole 1), entre ese factor primo
        multiplos = (num - 1) // primos[0]
        
        return (num - 1) - multiplos
    elif cant_primos == 2:

        producto = primos[0] * primos[1]

        p1 = (num - 1) // primos[0]
        p2 = (num - 1) // primos[1]
        # Dado que estamos contado múltiplos repetidos, entonces agarramos el producto entre p1 y p2, y calculamos la
        # cantidad de múltiplos (de tal número) que hay debajo de 'n'
        restar = (num - 1) // producto

        resultado = (p1 + p2) - restar

        return (num - 1) - resultado
    # Para cuando el número utiliza 3 o más factores primos únicos
    else:
        
        i = 0
        j = i + 1
        
        # Primero, se calculan todos los productos posibles usando dos números de la lista de los factores primos
        while i < cant_primos - 1:
            
            copia_primos = primos.copy()
        
            producto = copia_primos[i] * copia_primos[j]
            total.append(producto)
            fin += 1

            # Después, se hace un tipo de 'fusión'
            # En palabras simples, se crea una nueva lista, y se quita los dos números que se multiplicaron
            # y en su lugar, se pone el producto de esos dos números. Posteriormente, se agregan el resto de números
            # Ejemplo: [2,3,5,7] ----> [6,5,7]
            copia_primos.pop(i)
            copia_primos.pop(j - 1)
            copia_primos.append(producto)

            lista_fusiones.append(copia_primos)

            if j == cant_primos - 1:

                # Cuando llega al final del arreglo, la variable 'j' toma el valor de 'i' y se le suma 1
                # Esto se hace para evitar que haya repeticiones
                i += 1
                j = i + 1
            else:

                j += 1

        # Se pone en una lista, el conjunto de los productos que se pueden formar utilizando dos números de la lista de
        # los factores primos
        lista_conjuntos.append(total[inicio:fin])
        inicio = fin
        
        while True:

            # Si en la lista de fusiones, sólo quedan dos números, entonces se agarra el primer elemento
            # y se multiplican los dos números, debido a que el resto de elementos va a dar lo mismo
            if len(lista_fusiones[0]) == 2:

                total.append(lista_fusiones[0][0] * lista_fusiones[0][1])
                break

            lista_combinaciones = []
        
            cant_primosLista = len(lista_fusiones[0])
            
            # Se recorre por cada lista de fusiones
            for f in lista_fusiones:

                i = 0
                j = i + 1

                # Se hace los mismo que hicimos en la línea 71
                while i < cant_primosLista - 1:

                    copia_primos = f.copy()
        
                    producto = copia_primos[i] * copia_primos[j]
                    
                    # Verifica si el producto no está repetido en la lista donde están todos los productos posibles de crear
                    if not any(c == producto for c in total):
                    
                        total.append(producto)
                        fin += 1

                    copia_primos.pop(i)
                    copia_primos.pop(j - 1)
                    copia_primos.append(producto)

                    lista_combinaciones.append(copia_primos)

                    if j == cant_primosLista - 1:

                        i += 1
                        j = i + 1
                    else:

                        j += 1

            lista_fusiones = lista_combinaciones.copy()
            
            # Se agrega un conjunto de todos los posibles productos que se pueden formar usando 'x' cantidad de factores primos
            lista_conjuntos.append(total[inicio:fin])
            inicio = fin
    
    # En la lista de conjuntos, se agrega el producto de todos los factores primos
    lista_conjuntos.append([total[-1]])
    cant_noCoprimos = 0

    # Para encontrar la cantidad de números coprimos de 'n', se debe agarrando cada factor primo único, y calcular
    # la cantidad de múltiplos (de ese factor primo) que hay debajo de 'n'.
    # Los productos que calculamos anteriormente, nos servirá para ajustar la respuesta, y así obtener un resultado correcto
    for l in range(0, len(lista_conjuntos), 1):
        
        # Si la posición en el arreglo es par, entonces se suma. Si no, se resta
        operador = (-1) ** l
        valor = 0 # Almacena la cantidad de múltiplos
        for n in lista_conjuntos[l]:

            valor += (num - 1) // n

        cant_noCoprimos += (valor * operador)
    
    # Finalmente, se retorna la substracción
    # '(num - 1)' se refiere a la cantidad de números naturales que hay debajo de 'n'
    return (num - 1) - cant_noCoprimos

def main():
    
    n = 2
    limite = 1000000

    maximo = 0
    respuesta = 0

    while n <= limite:

        cociente = (n / funcionPhi(n))

        if cociente > maximo:

            maximo = cociente
            respuesta = n

        n += 2

    print(maximo)
    print(respuesta)

main()