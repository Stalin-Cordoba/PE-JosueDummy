# Utilizamos la fórmula de los números triangulares
# Resulta que, la cantidad de rectangulos que pueden haber en la cuadrícula, puede determinarse simplemente
# con el uso de esta fórmula
def numeroTriangular(n):

    return (n * (n + 1)) // 2

def main():

    # La cantidad de rectángulos a calcular no debe exceder 2 millones
    limite = 2000000

    l = 0
    h = 0
    
    respuesta_area = 0 # El problema nos pregunta el área de la cuadrícula rectangular
    dif_minima = None # La diferencia mínima entre 2 millones y la cantidad de rectángulos de una cuadrícula rectangular
    
    largo = 1
    alto = 1

    # Por medio de un poco de análisis, el largo puede ser cómo máximo de 1999
    while largo < 2000:

        while alto < 2000:
        
            # Se calcula la cantidad de triángulos que contiene la cuadrícula formada
            cant_rectangulos = numeroTriangular(largo) * numeroTriangular(alto)

            diferencia = limite - cant_rectangulos

            # Si la diferencia empieza a dar en negativo, se rompe el ciclo
            if diferencia < 0:

                break
            # La cuadrícula rectangular que tenga la menor diferencia con 2 millones, es la respuesta
            elif dif_minima == None or (dif_minima > diferencia):

                l = largo
                h = alto
                dif_minima = diferencia
                respuesta_area = largo * alto

            alto += 1
        
        largo += 1
        alto = 1

    print(f"{respuesta_area} ({l}x{h})")

main()