from math import log10

def factorial(numero):

    fact = 1

    for i in range(numero, 0, -1):

        fact *= i

    return fact

# Los factoriales para cada dígito del número
def factDigitos(num):

    str_num = str(num)
    suma = 0

    for d in str_num:

        digito = int(d)
        suma += factorial(digito)

    return suma

def main():

    num_inicial = 2 # El número con el que se empieza (No se inicia con 1, porque el factorial de uno, da uno xd)
    respuesta = 0

    while num_inicial < 1000000:

        # Si el número es una potencia de 10, se omite de viaje
        if log10(num_inicial).is_integer():
        
            num_inicial += 1
        else:

            terminos = [num_inicial] # Términos de la secuencia, donde se incluye el número con el que se empieza
            cant_terminos = 1

            while True:
            
                # Para calcular el siguiente término, se utiliza el último elemento que hay en la lista
                siguiente_termino = factDigitos(terminos[-1])

                estaRepetido = True

                # Verifica si el término no está repetido
                try:

                    terminos.index(siguiente_termino)
                except ValueError:

                    estaRepetido =  False
                    terminos.append(siguiente_termino)
                    cant_terminos += 1

                # Si está repetido, no se sigue agregando más elementos
                if estaRepetido:

                    break

            # La cantidad de términos debe ser EXACTAMENTE 60
            if cant_terminos == 60:

                respuesta += 1

            num_inicial += 1

    print(respuesta)

main()