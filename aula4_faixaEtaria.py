idadeMenorIgual15, idadeMaior15 = 0,0

while True:
    idade = int(input("Digite uma idade(Negativo para sair): "))

    if idade < 0:
        break
    elif idade <= 15:
        idadeMenorIgual15 += 1
    else:
        idadeMaior15 += 1

print("Menor ou igual a 15: %d." % idadeMenorIgual15)
print("Maior que 15: %d." % idadeMaior15)
