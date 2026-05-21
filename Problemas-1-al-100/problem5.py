def main():

    num = 1
    i = 2

    while True:

        if num % i == 0:

            i += 1

            if i > 12:

                break
        else:

            i = 2
            num += 1

    print(num)

main()