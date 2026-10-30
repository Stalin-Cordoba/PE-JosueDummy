from math import sqrt, floor

def areaEntera(base, perimetro):

    # Se usa la fórmula de Herón para el área
    # Al simplificarla con los datos que nos da el problema, obtendremos (dentro de la raíz cuadrada):
    # s * (s - c)
    c = base

    s = perimetro // 2

    s_c = s - c # Calculamos (s - c)
    producto = s * s_c # Multiplicamos 's' con '(s - c)'

    # Del producto de 's' entre '(s - c)', determinamos su raíz cuadrada
    # Sin embargo, sólo queremos saber si la raíz da como resultado, un número entero o un número irracional
    # Esto es debido a que, si es un número irracional, no tiene sentido determinar si el área del triángulo es
    # entera, porque multiplicar un número entero, con un número irracional, JAMÁS dará como resultado, un número entero
    raiz = sqrt(producto)

    # Por lo tanto, si la raíz cuadrada NO es exacta, entonces el área de ese triángulo NO ES entera
    if not raiz.is_integer():

        return False
    else:

        # Ahora, si la raíz cuadrada es exacta, se verifica si es verdad
        # Parece innecesario, pero algo que ocurre, es que cuando se intenta sacar la raíz cuadrada de un número
        # muy grande, Python puede (sin querer) redondear el resultado de una raíz cuadrad que no es exacta, lo que
        # impide que nos de la respuesta correcta
        raiz = floor(raiz)

        # Se elevado al cuadrado el número obtenido por la raíz
        verifcacion = raiz ** 2

        # Se calcula la diferencia entre el número que elevamos al cuadrado y el producto: s * (s - c)
        diferencia = producto - verifcacion

        # Si la diferencia es 0, entonces el número que elevamos al cuadrado, es en efecto, igual a: s * (s - c)
        if diferencia == 0:

            return True
        # Si no es así, entonces la raíz cuadrada, efectivamente no es exacta
        else:

            return False

def main():

    respuesta = 0

    # Empezamos con 3
    # Para los lados que tienen que ser iguales, sólo usamos números impares
    # Con un poco de análisis, es posible demostrar que no existe un triángulo casi equilátero con
    # área entera, que tiene:
    # 2 lados iguales, cuyas medidas, son un número par
    # 1 lado desigual, cuya medida, es un número impar
    for i in range(3, 333333334, 2):

        perimetro = (2 * i) + (i + 1)

        if areaEntera(i + 1, perimetro):

            respuesta += perimetro

        perimetro = (2 * i) + (i - 1)
        
        if areaEntera(i - 1, perimetro):
        
            respuesta += perimetro

    print(respuesta)

main()