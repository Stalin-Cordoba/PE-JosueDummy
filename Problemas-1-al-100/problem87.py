from math import sqrt, trunc

def listaPrimos(max):

    # Agregamos el 2
    numerosPrimos = [2]
    limite = trunc(sqrt(max)) # Se calcula el número máximo que, al elevarlo al cuadrado, da menos que 50 millones

    # Para ahorrar tiempo, sólo se listan los números impares (excepto el 1)
    for i in range(3, limite + 1, 2):

        numerosPrimos.append(i)
    
    ultimoNumero = numerosPrimos[-1]

    # Como no están los pares, excluimos el dos para el ciclo 'for'
    for divisor in numerosPrimos[1::]:

        if divisor >= sqrt(ultimoNumero):

            break
        else:
            for num in numerosPrimos:

                # Revisa todos los múltiplos de cada número en la lista
                if num % divisor == 0 and num != divisor:

                    del numerosPrimos[numerosPrimos.index(num)]

    return numerosPrimos

def fin_para_S(primos, max):

    for p in primos:

        if not (p ** 4 < max):

            return primos.index(p)
        
def fin_para_Q(primos, max):

    for p in primos:

        if not (p ** 3 < max):

            return primos.index(p)

# La función sólo devuelve la cantidad de números que hay en la lista
def unicos(lista):

    # Ordenamos la lista original
    listaOrdenada = sorted(lista.copy())

    conteo = 1

    # Empezamos desde el segundo elemento
    for i in range(1, len(listaOrdenada), 1):

        # Para validar si el número no es repetido, se verifica si el anterior no es igual que él
        if listaOrdenada[i] != listaOrdenada[i - 1]:

            conteo += 1

    return conteo

def main():

    maximo = 50000000
    primos = listaPrimos(maximo)

    # La 'i' significa 'Inicio del rango' y la 'f' significa 'Final del rango'
    # La otra letra representa la lista que pertenece tal rango
    i_S = 0
    f_S = fin_para_S(primos, maximo)

    i_Q = f_S
    f_Q = fin_para_Q(primos, maximo)

    i_L = f_Q
    
    # 'S' contiene los números que pueden elevarse al cuadrado, al cubo, y a la cuarta potencia, sin pasarse del máximo permitido
    # 'Q' contiene los números que pueden elevarse al cuadrado y al cubo, pero NO a la cuarta potencia, porque sino se pasan del máximo
    # 'L' contiene los números que solamente pueden elevarse al cuadrado, porque elevarlos al cubo o a la 4, se pasarían del máximo
    S = primos[i_S:f_S]
    Q = primos[i_Q:f_Q]
    L = primos[i_L::]

    a = 0
    b = 0
    c = 0

    numeros = [] # Cada producto lo almacenamos en una lista (ya verás por qué)

    while a < len(S):

        producto = S[a] ** 2 + S[b] ** 3 + S[c] ** 4
        if producto < maximo:
            
            numeros.append(producto)

        if c == len(S) - 1:

            if b == len(S) - 1:

                a += 1
                b = 0
                c = 0
            else:

                b += 1
                c = 0
        else:

            c += 1

    a = 0

    while a < len(Q):

        while b < len(S):

            producto = Q[a] ** 2 + S[b] ** 3 + S[c] ** 4
            if producto < maximo:
            
                numeros.append(producto)

            if c == len(S) - 1:

                b += 1
                c = 0
            else:

                c += 1

        b = 0

        while b < len(S):

            producto = S[b] ** 2 + Q[a] ** 3 + S[c] ** 4
            if producto < maximo:
            
                numeros.append(producto)

            if c == len(S) - 1:

                b += 1
                c = 0
            else:

                c += 1

        b = 0
        a += 1

    a = 0

    while a < len(Q):

        b = 0

        while b < len(Q):

            producto = Q[a] ** 2 + Q[b] ** 3 + S[c] ** 4
            if producto < maximo:
            
                numeros.append(producto)

            if c == len(S) - 1:

                b += 1
                c = 0
            else:

                c += 1

        a += 1

    a = 0
    
    while a < len(L):

        b = 0

        while b < len(S):

            producto = L[a] ** 2 + S[b] ** 3 + S[c] ** 4
            if producto < maximo:
            
                numeros.append(producto)

            if c == len(S) - 1:

                b += 1
                c = 0
            else:

                c += 1

        b = 0

        while b < len(Q):

            producto = L[a] ** 2 + Q[b] ** 3 + S[c] ** 4
            if producto < maximo:
            
                numeros.append(producto)

            if c == len(S) - 1:

                b += 1
                c = 0
            else:

                c += 1

        a += 1

    # Calculamos la cantidad de formas de sumar un primo al cuadrado, un primo al cubo, y un primo a la cuarta potencia
    # Sin embargo, puede exisitr un número que se puede escribir de la manera que se acaba de describir
    # Ejemplo:
    # 2^2 + 5^3 + 2^4 = 145 y 11^2 + 2^3 + 2^4 = 145
    # Por lo tanto, de la lista 'numeros', sólo extraemos la cantidad de números únicos que hay
    # Y esa sería nuestra respuesta
    print(f"Respuesta: {unicos(numeros)}")

main()