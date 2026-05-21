def main():

    mayorParteDecimal = 0
    respuesta = 0
    
    for d in range(2, 1000, 1):

        parteDecimal = "0."

        num = 10
    
        for i in range(1, 10000, 1):
        
            while True:

                if d > num:

                    num *= 10
                    parteDecimal += "0"
                else:

                    break

            cociente = num // d
            parteDecimal += str(cociente)

            residuo = num % d

            if residuo == 0:

                break
            else:
                num = residuo
                num *= 10

        aumento = 0
        diferencia = 1
        # Compara 5 partes decimales
        while True:
        
            dI_0 = 2 + aumento
            dF_0 = dI_0 + diferencia

            dI_1 = dF_0
            dF_1 = dI_1 + diferencia

            dI_2 = dF_1
            dF_2 = dI_2 + diferencia

            dI_3 = dF_2
            dF_3 = dI_3 + diferencia

            dI_4 = dF_3
            dF_4 = dI_4 + diferencia

            if dF_4 > len(parteDecimal) - 1:

                if dI_0 > len(parteDecimal) - 1:

                    print(f"1/{d} no tiene parte periodica")
                    break
                else:
                    aumento += 1
                    diferencia = 1
            else:

                comparacion = parteDecimal[dI_0:dF_0]

                pt1 = parteDecimal[dI_1:dF_1]
                pt2 = parteDecimal[dI_2:dF_2]
                pt3 = parteDecimal[dI_3:dF_3]
                pt4 = parteDecimal[dI_4:dF_4]

                if comparacion == pt1 and comparacion == pt2 and comparacion == pt3 and comparacion == pt4:

                    print(f"Parte periodica de 1/{d}: {comparacion} ({len(comparacion)})")
                    if len(comparacion) > mayorParteDecimal:

                        mayorParteDecimal = len(comparacion)
                        respuesta = d
                    
                    break

                diferencia += 1

    print(f"Número con mayor parte periódica: {respuesta}")

main()