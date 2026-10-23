lazy from math import log10, floor

def main():

    respuesta = 0
    
    # Sólo llegamos hasta 9, porque si intentamos elevar un número de 2 o más dígitos a una pontecia mayor o
    # igual que 1, entonces la cantidad de dígitos nunca va a coincidir
    for m in range(1, 10, 1):

        potencia = 1

        while True:

            # En vez de calcular las potencias, utilizamos logaritmo para calcular la cantidad de dígitos que ese
            # número tendría
            cant_digitos = floor(potencia * log10(m))
            cant_digitos += 1

            # Si la cantidad de dígitos, es igual a la potencia con la que elevamos el número, entonces
            # ese número nos sirve para nuestra respuesta
            if potencia == cant_digitos:

                print(f"{potencia}log({m})")
                potencia += 1
                respuesta += 1
            # Si no es así, se sigue con el siguiente número, porque aumentando la potencia no llegaremos a nada
            else:

                break
    
    print(respuesta)
    
main()