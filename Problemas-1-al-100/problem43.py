def fact(num):

    producto = 1

    for i in range(num, 0, -1):

        producto *= i

    return producto

def main():
    
    combinaciones = []
    
    digitos = [0,1,2,3,4,5,6,7,8,9] # Un arreglo para los dígitos
    primos = [2,3,5,7,11,13,17]

    # Se calcula cada combinación
    for v in range(1, fact(10) + 1, 1):

        respuesta = ""
        
        digitos = [0,1,2,3,4,5,6,7,8,9]
        
        objetivo = v # El valor actual
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

        cumple_propiedad = True
        
        for n in range(1, len(primos) + 1, 1):

            if int(respuesta[n:(n+3)]) % primos[n - 1] != 0:

                cumple_propiedad = False
                break

        if cumple_propiedad:

            combinaciones.append(int(respuesta))

    print(combinaciones)
    print(sum(combinaciones)) # Se suma todas las combinaciones que cumplen la propiedad

main()