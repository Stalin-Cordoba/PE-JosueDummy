# Calcular el siguiente estado del contador binario
def contar_bin(contador):

    sig_estado = contador # Siguiente estado
    cant_digitos = len(contador)

    sig_estado[-1] += 1

    j = cant_digitos - 1

    while True:

        if sig_estado[j] == 2:

            if j > 0:
            
                sig_estado[j - 1] += 1

            sig_estado[j] = 0

            j -= 1
        else:

            break
    
    return sig_estado

def elegirNumeros(numeros, cont_bin):

    elegidos = []

    for k in range(0, len(cont_bin), 1):

        # Cada k-ésimo elemento del conjunto de las monedas, se compara con el k-ésimo dígito del contador binario
        # Si hay un 1, se elige el número. Si hay un 0, entonces no se elige el número
        if cont_bin[k] == 1:

            elegidos.append(numeros[k])

    return elegidos

def sumarMonedas(mone_eleg, coe):

    suma = 0

    for m in range(0, len(mone_eleg), 1):

        suma += (mone_eleg[m] * coe[m]) # Multiplica el valor de la moneda correspondiente con el coeficiente proporcionado

    return suma

def main():

    # Nota: No se incluye la moneda de 1 penique ni la de 2 libras, porque esas son muy obvias de utilizar xd
    monedas = [100, 50, 20, 10, 5, 2]

    # Se le asigna el valor de '2', porque ya tenemos dos combinaciones muy obvias:
    # 1. Una moneda de 2 libras esterlinas
    # 2. 200 monedas de 1 penique
    respuesta = 2

    objetivo = 200

    contador_bin = [0,0,0,0,0,0] # Se utiliza para elegir los números para las combinaciones
    
    contador_bin = contar_bin(contador_bin)

    while contador_bin != [0,0,0,0,0,0]:

        nums_elegidos = elegirNumeros(monedas, contador_bin) # Los números elegidos

        # Si sólo se eligió un número, entonces se divide 200 entre el número elegido
        if len(nums_elegidos) == 1:

            respuesta += objetivo // nums_elegidos[0]
        else:

            # Define la máxima cantidad de veces que la moneda de mayor valor pueda usarse
            maximo = (objetivo // nums_elegidos[0]) - 1
            cant_eleg = len(nums_elegidos) # Cantidad de números elegidos

            coeficientes = [] # Los coeficientes para cada moneda elegida

            # Todos los coeficientes empiezan con el valor de 1
            for i in range(0, len(nums_elegidos), 1):

                coeficientes.append(1)

            while coeficientes[0] <= maximo:

                suma = sumarMonedas(nums_elegidos, coeficientes) # La suma se calcula

                # El motivo por el cual verificamos si la suma es menor que 200. Se debe a que la cantida que falta,
                # puede llenarse con unos. Por ejemplo, si la suma da: 5 + 2 = 7, para completar el 200, se pueden usar
                # 193 unos.
                if suma > objetivo:
                    
                    coeficientes[-1] = 1

                    # En el arreglo de los números elegidos, nos ubicamos en el penúltimo elemento
                    r = cant_eleg - 2

                    while True:

                        # Se procede a agregar uno al coeficiente correspondiente
                        coeficientes[r] += 1

                        # Si al coeficiente que le acabamos de sumar 1, al realizar la suma, nos da un valor mayor que
                        # 200, entonces se va con otro
                        if sumarMonedas(nums_elegidos, coeficientes) > objetivo:
                            
                            # Si la moneda con mayor valor ya llegó a su límite de usos, entonces ahí
                            # se termina el ciclo para ese conjunto de monedas
                            if coeficientes[0] > maximo:

                                break
                            
                            coeficientes[r] = 1
                            r -= 1 # Se va al anterior
                        # Si no es así, entonces se continúa normal
                        else:

                            break
                else:

                    respuesta += 1
                    coeficientes[-1] += 1
            
        contador_bin = contar_bin(contador_bin) # Siguiente estado
    
    print(respuesta)

main()