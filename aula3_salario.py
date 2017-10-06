salario = float(input("Qual o seu salário? "))

if salario < 300:
    print("Novo salário R$%.2f" % (salario*1.45))
if 300 <= salario <= 600:
    print("Novo salário R$%.2f" % (salario*1.25))
if salario > 600:
    print("Novo salário R$%.2f" % (salario*1.15))
