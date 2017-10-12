while True:
    codigo = int(input("Digite o código do produto(1,2,3 ou 4 / 0 para sair): "))

    if codigo == 1:
        print("Caderno - R$ 12.00")
        valor = 12
    elif codigo == 2:
        print("Régua - R$ 2.50")
        valor = 2.5
    elif codigo == 3:
        print("Borracha - R$ 0.25")
        valor = 0.25
    elif codigo == 4:
        print("Mochila - R$ 50.00")
        valor = 50
    elif codigo == 0:
        break
    else:
        print("Código inválido!")

    qnt = int(input("Quantidade: "))

    print("Total a pagar: R$%.2f" % (valor*qnt))
