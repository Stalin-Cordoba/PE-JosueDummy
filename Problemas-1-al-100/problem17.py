def main():

    total_letrasUtil = 0
    
    # NOTA: Los números deben ser escritos en inglés
    # Aquí incluimos los números que son especiales
    numeros_1_al_19 = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight'
                       , 9: 'nine',10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen'
                       , 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    
    # Estos números pueden ser combinados con una unidad
    # Ejemplo: Twenty-six (26)
    numeros_desde_20 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    
    # Las centenas, que tiene que llevar 'and', una decima, y una unidad
    centenas = {1: 'onehundred', 2: 'twohundred', 3: 'threehundred', 4: 'fourhundred'
                , 5: 'fivehundred', 6: 'sixhundred', 7: 'sevenhundred', 8: 'eighthundred', 9: 'ninehundred'}


    for n in range(1, 20, 1):

        total_letrasUtil += len(numeros_1_al_19[n])
    
    for n in range(20, 100, 1):

        cadena = ""
        num = n

        decima = num // 10
        cadena += numeros_desde_20[decima]

        unid = num - (decima * 10)
        cadena += numeros_1_al_19[unid]

        total_letrasUtil += len(cadena)

    for n in range(100, 1000, 1):

        cadena = ""
        numero = n
    
        # Primero, se calcula la centena
        centena = numero // 100
        cadena += centenas[centena]
        numero -= (centena * 100) # Se reduce el número para obtener la decima

        if numero > 0 and numero < 20:

            cadena += "and"
            cadena += numeros_1_al_19[numero]
        elif numero >= 20:

            cadena += "and"

            decima = numero // 10
            cadena += numeros_desde_20[decima]

            numero -= (decima * 10) # Se reduce el número para obtener la unidad

            cadena += numeros_1_al_19[numero]

        total_letrasUtil += len(cadena)

    # Tiene que terminar en 1000, pero sólo incluimos cuántas letras tiene 'OneThousand' (que es 11)
    total_letrasUtil += 11
    
    print(f"Total de letras para escribir los números del 1 al 100: {total_letrasUtil}")

main()