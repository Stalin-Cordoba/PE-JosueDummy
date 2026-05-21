def main():

    numero = str(2 ** 1000) # Se convierte la operación en string
    suma = 0

    for e in numero:

        suma += int(e) # Como todo el número se volvió String, cada número se vuelve entero

    print(suma)

main()