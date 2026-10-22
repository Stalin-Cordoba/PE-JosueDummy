# NOTA: La lista con la que se trabaja es de 3 elementos (excluyendo el cuarto elemento, porque es un número cuadrado)
def determinarPrimos(numeros, cant_filas):
    
    # En vez de poner un ciclo 'for' para cada número, se ponen los tres de un solo xdxd
    
    p1 = numeros[0]
    p2 = numeros[1]
    p3 = numeros[2]
    
    # Dado que el último número del espiral cuadrado, es un número elevado al cuadrado, podemos
    # usar esto a nuestro favor para establecer el límite
    limite = cant_filas

    for i in range(3, limite, 2):

        # Si uno resulta no ser primo, se le asigna el valor de 0 por el resto del ciclo 'for'
        # Esto sirve para dos cosas:
        # 1. Para calcular el conteo (en vez de crear una variable booleana para los tres números)
        # 2. Dejar un resultado fijo (XD)
        if p1 % i == 0 and p1 != 0:

            p1 = 0
        if p2 % i == 0 and p2 != 0:

            p2 = 0
        if p3 % i == 0 and p3 != 0:

            p3 = 0

    # Dado que los valores que siempre comparamos siempre son números impares, entonces dividimos entre 2, y
    # sólo devolvemos el residuo entero, para calcular el conteo
    # Recordatorio: 0 % 2 = 0
    conteo = (p1 % 2) + (p2 % 2) + (p3 % 2)

    return conteo

def porcentajePrimos(primos, total_diagonales):

    return primos / total_diagonales

def main():
    
    salto = 2
    num_filas = 3
    numero_empezar = 1
    numero_anterior = numero_empezar

    cant_diagonales = 1 # Cantidad de números diagonales
    cant_primos = 0 # Cantidad de números primos en las diagonales

    while True:

        numeros_diagonales = []

        # Se calculan los números diagonales de la nueva capa
        for i in range(0, 4, 1):

            p = numero_anterior + salto

            numeros_diagonales.append(p)

            numero_anterior = p

        cant_primos += determinarPrimos(numeros_diagonales[0:3], num_filas)

        numero_anterior = numeros_diagonales[-1]
        cant_diagonales += 4 # Al agregar una nueva capa, aparecen 4 nuevos números en las diagonales del espiral cuadrado

        porcentaje = porcentajePrimos(cant_primos, cant_diagonales)
        if porcentaje < 0.1:

            print("Respuesta:", num_filas)
            print("Porcentaje:", porcentaje)
            break

        salto += 2 # En cada capa, la diferencia que tienen los números diagonales entre ellos es una potencia de 2
        num_filas += 2 # Al agregar una capa al espiral cuadrado, la cantidad de filas aumenta en 2

main()