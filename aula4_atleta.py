while True:
    deltaX = float(input("Distância percorrida: "))
    deltaT = float(input("Tempo gasto: "))

    print("Sua velocidade foi de %.2f!" % (deltaX/deltaT))

    opcao = input("Deseja continuar(s/n): ")
    if opcao == "n":
        break
