maior = 0

for i in range(10):
    valor = float(input("Qual o valor? "))
    if valor > maior:
        maior = valor

print("O maior valor foi: %.2f" % maior)
