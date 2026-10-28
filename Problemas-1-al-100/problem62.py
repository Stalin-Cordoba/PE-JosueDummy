from math import cbrt, floor

def digitosUtilizados(numero):

    num_str = str(numero)
    listaDigitos = []

    for i in num_str:

        listaDigitos.append(int(i))

    return sorted(listaDigitos)

def main():

    respuestaEncontrada = False
    potencia_diez = 10

    num_actual = 1

    while True:
        
        # Por cada potencia de diez, se le pone un límite, utilizando la raíz cúbica
        # Esto se hace para que los cubos a generar, tengan la misma cantidad de dígitos
        lim = floor(cbrt(potencia_diez))
        
        combinaciones = []
        cubos = []

        # Se generan todos los cubos debajo del límite
        while num_actual < (lim + 1):

            cubo = num_actual ** 3

            # Se determina los dígitos utilizados por cada cubo
            comb = digitosUtilizados(cubo)

            cubos.append(cubo)
            combinaciones.append(comb)

            num_actual += 1

        # Recorre la lista de todas las combinaciones/permutaciones realizadas
        # Se usa 'range' para determinar el cubo que generó esa permutación de dígitos
        for j in range(0, len(combinaciones), 1):

            # Si hay un cubo, donde 4 otros cubos distintos, ocupan los mismo dígitos, esa es nuestra respuesta
            if combinaciones.count(combinaciones[j]) == 5:

                print(cubos[j])
                respuestaEncontrada = True
                break

        # Si se encontró la respuesta, se termina el ciclo
        if respuestaEncontrada:

            break
        # En caso contrario, se repite todo el proceso
        else:

            potencia_diez *= 10

main()