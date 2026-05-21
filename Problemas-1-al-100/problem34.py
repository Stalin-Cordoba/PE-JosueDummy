def factorial(num):

    fact = 1
    for n in range(num, 0, -1):

        fact *= n

    return fact

def main():

    resultado = 0
    
    for num in range(3, 1000001, 1):

        texto_num = str(num)
        suma = 0

        for digito in texto_num:

            suma += factorial(int(digito))

        if suma == num:

            resultado += num

    print(resultado)

main()