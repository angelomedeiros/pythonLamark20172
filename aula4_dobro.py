while True:
    n = float(input("Digite um número(Número negativo sai): "))

    if n < 0:
        break

    print("O dobro do número digitado é %.2f!" % (n*2))
