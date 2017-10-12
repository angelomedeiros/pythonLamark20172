for i in range(10):
    n = float(input("Digite um número: "))
    print("O triplo do número digitado é %.2f" % (3*n))

    if n > 0:
        print("O número digitado é positivo!")
    elif n < 0:
        print("O número digitado é negativo!")
    else:
        print("O número digitado é nulo!")
