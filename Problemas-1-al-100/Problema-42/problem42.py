from math import sqrt

def main():

    with open('Problemas-1-al-100/Problema-42/0042_words.txt', 'r') as palabras:

        lineaCompleta = palabras.readline()
    
    letras = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    conteo = 0

    for palabra in lineaCompleta.split(','):

        suma = 0
        palabra = palabra.replace('"','')
        
        for letra in palabra:

            suma += letras[letra]

        suma *= 2

        if formulaCuadratica(suma):

            conteo += 1

    print(conteo)

def formulaCuadratica(numero):

    resultado = (1 + sqrt(1 + (4 * numero))) / 2

    if resultado % 1 == 0.0:

        return True
    else:

        return False

main()