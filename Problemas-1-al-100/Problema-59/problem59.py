import os

# Útil para el XOR
def decimal_a_Binario(num):

    # Se trabajará con 8 bits
    binario = ""

    for p in range(7, -1, -1):

        if num >= (2 ** p):

            binario += "1"
            num -= (2 ** p)
        else:

            binario += "0"

    return binario

def binario_a_Decimal(binNum):

    p = 7 # Potencia
    resultado = 0

    for j in range(0, 8, 1):

        resultado += (int(binNum[j])) * (2 ** p)

        p -= 1

    return resultado

def xor(bin1, bin2):

    resultado = ""
    
    for i in range(0, 8, 1):

        # Si el dígito correspondiente del primer número binario, es igual que el del segundo número binario, entonces
        # se agrega un '0', porque los dos dígitos no pueden ser iguales
        if bin1[i] == bin2[i]:

            resultado += "0"
        else:

            resultado += "1"

    return resultado

def main():

    with open('Problemas-1-al-100/Problema-59/0059_cipher.txt') as texto_plano:

        texto = texto_plano.readline()
    
    # La clave está compuesta de tres letras minúsculas
    # Los valores que puede tener es de 97 hasta 122 (de la 'a' a la 'z')
    l1 = 97
    l2 = 97
    l3 = 97

    while l1 <= 122:

        chars_encriptados = texto.split(',') # Caracteres Encriptados

        # Se convierten a binario cada carácter de la clave
        k1 = decimal_a_Binario(l1)
        k2 = decimal_a_Binario(l2)
        k3 = decimal_a_Binario(l3)

        texto_original = ""
        suma_caracteres = 0

        # Hay un total de 1455 caracteres encriptados. Como la clave es de 3 caracteres, entonces
        # 1455 / 3 = 485
        for i in range(0, len(chars_encriptados) - 2, 3):

            # Cada caracter encriptado se convierte a binario
            b_c1 = decimal_a_Binario(int(chars_encriptados[i]))
            b_c2 = decimal_a_Binario(int(chars_encriptados[i + 1]))
            b_c3 = decimal_a_Binario(int(chars_encriptados[i + 2]))
        
            # Se les aplica XOR con los caracteres de la clave respectivamente
            c1 = xor(b_c1, k1)
            c2 = xor(b_c2, k2)
            c3 = xor(b_c3, k3)

            # Se convierten a decimal
            c1 = binario_a_Decimal(c1)
            c2 = binario_a_Decimal(c2)
            c3 = binario_a_Decimal(c3)

            # Los caracteres se adjuntan
            texto_original += chr(c1)
            texto_original += chr(c2)
            texto_original += chr(c3)

            suma_caracteres += c1 + c2 + c3

        # Se imprime el texto que se obtuvo
        print(texto_original)
        print(f"Clave: {chr(l1)}{chr(l2)}{chr(l3)}") # Se imprime la clave que se utilizó

        detenerBucle = False

        while True:

            try:

                # Lo complicado en este problema, es que es opción del usuario de continuar el ciclo
                # El bucle continúa hasta que el texto que se obtuvo sea legible
                # Cuando el texto sea legible, el usuario debe parar el bucle para así obtener la respuesta
                respuesta = input("¿Continuar bucle (Elige 'N' si el texto es legible)? (Y/N)")
                
                if respuesta.lower() == 'n':
                
                    detenerBucle = True
                    break
                elif respuesta.lower() == 'y':

                    break
                else:

                    print("Ingrese una opción correcta")
            except:

                print("Ingrese correctamente su respuesta")

        if detenerBucle:

            break

        # Limpia la terminal
        os.system('cls')

        l3 += 1

        # El límite es 122
        if l3 == 123:

            l3 = 97
            l2 += 1

            if l2 == 123:

                l2 = 97
                l1 += 1

    os.system('cls')
    
    # Resultados
    print("\n---TEXTO ORIGINAL---")
    print(texto_original)
    print(f"Clave: {chr(l1)}{chr(l2)}{chr(l3)}")
    print("Suma de caracteres ASCII:", suma_caracteres)

main()