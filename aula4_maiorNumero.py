maior = 0

while True:
    n = float(input("Digite um número(0 para sair): "))

    if n > maior:
        maior = n
    elif n == 0:
        break

print("Maior número: %d" %maior)
