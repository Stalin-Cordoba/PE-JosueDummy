from math import sqrt, floor

def digitosUtilizados(numero):

    num_str = str(numero)
    listaDigitos = []

    for i in num_str:

        listaDigitos.append(int(i))

    return sorted(listaDigitos)

def esPrimo(n):

    limite = floor(sqrt(n))

    for i in range(2, limite, 1):

        if n % i == 0:

            return False

    return True

def main():

    N = 10000000
    
    Primos = [2]

    # Se calculan los primos menores que 5000000
    for i in range(3, N // 2, 2):

        if esPrimo(i):

            Primos.append(i)

    cant = len(Primos)

    minimo = None

    # Cómo nos piden el mínimo, fácilmente podríamos encontrar el primo más grande debajo de 10 millones, pero como nos pide
    # que el resultado, sea una permutación de tal número, no nos sirve.
    # En vez de evaluar la función phi para cada número, podemos determinar los números que sólo tienen dos factores primos,
    # y así encontrar el mínimo más rápido
    for i in range(0, cant, 1):

        for j in range(i, cant, 1):

            producto = Primos[i] * Primos[j]

            if producto > 10000000:

                break
            else:
                phi = producto * (1 - (1 / Primos[i])) * (1 - (1 / Primos[j]))

                phi = floor(phi)

                if digitosUtilizados(phi) == digitosUtilizados(producto):

                    division = producto / phi

                    if minimo == None or minimo > division:

                        n = producto
                        phi_n = phi
                        minimo = division

    print(f"n = {n} | phi = {phi_n}")
    print(minimo)

main()