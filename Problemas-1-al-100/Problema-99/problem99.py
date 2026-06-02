from math import log10

def leerTexto():

    with open('Problemas-1-al-100/Problema-99/0099_base_exp.txt', 'r') as texto:

        numeros = texto.read()

    return numeros

def main():

    # Obtenemos el texto que se leyó y se divide los saltos de línea
    listaNumeros = leerTexto().split('\n')

    # Del primer elemento, se divide la base y el exponente    
    primerElemento = listaNumeros[0].split(',')

    base = int(primerElemento[0])
    expo = int(primerElemento[1])

    # Para manejar con números extremadamente grandes, usamos logaritmos
    # Se multiplica el logaritmo base 10 de la base, por el exponente
    productoMayor = expo * log10(base)
    posicion = 1
    
    mayor = base
    mayor_posicion = 1 # Marca la posición de línea donde está el mayor valor

    for numero in listaNumeros[1::]:

        posicion += 1
        numeroDescompuesto = numero.split(',') # Descomponemos el número, para obtener su base y exponente
        
        base_comp = int(numeroDescompuesto[0])
        expo_comp = int(numeroDescompuesto[1])

        producto_comp = expo_comp * log10(base_comp)

        # Si el producto es mayor
        if producto_comp > productoMayor:

            mayor_posicion = posicion
            mayor = base_comp
            productoMayor = producto_comp

    print(f"{mayor} (Posición: {mayor_posicion})")

main()