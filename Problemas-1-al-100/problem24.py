def fact(num):

    producto = 1

    for i in range(num, 0, -1):

        producto *= i

    return producto

def main():

    respuesta = ""
    
    digitos = [0,1,2,3,4,5,6,7,8,9] # Un arreglo para los dígitos

    objetivo = 1000000 # La permutación que deseamos buscar
    suma = 0

    for n in range(9, -1, -1):

        i = 0
        while True:

            # Para el i-esimo dígito, se calculan las combinaciones totales para el resto de espacios sin dígitos
            # Si la suma no llega al objetivo establecido, se sigue con el siguiente dígito
            suma += fact(n)

            if suma >= objetivo:

                suma -= fact(n)
                break
            else:

                i += 1

        respuesta += str(digitos[i])
        digitos.pop(i) # Una vez utilizado un dígito, se quita del arreglo

    print(respuesta)
main()