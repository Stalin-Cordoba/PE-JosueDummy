def abundancia(numero):

    suma = 1
    
    for i in range(2, numero, 1):

        if numero % i == 0:

            suma += i

    return suma > numero

def main():

    numerosAbundantes = []
    
    for n in range(12, 28124, 1):

        if abundancia(n):

            numerosAbundantes.append(n)

    resultado = 276
    
    # Empezamos por el '25'
    for num in range(24, 28124, 1):

        sumaDosAbundantes = False
        for i in range(0, len(numerosAbundantes), 1):

            for j in range(i, len(numerosAbundantes), 1):

                if num == numerosAbundantes[i] + numerosAbundantes[j]:

                    sumaDosAbundantes = True
                    break
                elif numerosAbundantes[i] + numerosAbundantes[j] > num:

                    break

            if sumaDosAbundantes or numerosAbundantes[i] > num:

                break

        if not sumaDosAbundantes:

            resultado += num

    print(resultado)
                
main()