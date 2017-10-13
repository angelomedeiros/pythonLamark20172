valor = [float(input("valor: ")) for i in range(5)]
i50 = [x for x in valor if x<50]
i80s50 = [y for y in valor if 50<=y<=80]
s80 = [z for z in valor if z>80]
print("Inferior a 50: {}\nEntre 50 e 80: {}\nSuperior a 80: {}\nMédia: {}" .format(len(i50),len(i80s50),len(s80),(sum(valor)/5)))

