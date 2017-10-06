n1 = float(input("Digite o primeiro número? "))
n2 = float(input("Digite o segundo número? "))

print("Digite 1 ou 2 para saber qual o maior número digitado!")
print("Digite 3 ou 4 para saber qual o menor número digitado!")

ope = int(input("Digite o número da operação: "))

if ope == 1 or ope == 2:
    if n1 > n2:
        print("O número %f é maior!" % n1)
    elif n1 < n2:
        print("O número %f é maior!" % n2)
    else:
        print("Os números são iguais!")
elif ope == 3 or ope == 4:
    if n1 > n2:
        print("O número %f é menor!" % n2)
    elif n1 < n2:
        print("O número %f é menor!" % n1)
    else:
        print("Os números são iguais")
else:
    print("ERRO: Operação inválida")

