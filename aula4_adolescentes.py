adolescentes = 0

while True:
    idade = int(input("Digite a idade(número negativo sai): "))

    if 12 <= idade <= 17:
        adolescentes += 1
    elif idade < 0:
        break

print("Adolescentes(entre 12 e 17 anos): %d" % adolescentes)
