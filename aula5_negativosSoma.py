numeros = [float(input("Digite um número: ")) for i in range(4)]
negativos = list(filter(lambda x: x<0, numeros))
#positivos = list(set(numeros)-set(negativos))
positivos = [x for x in numeros if x>0]
print("Negativos: {}\nSoma positivos: {}" .format(len(negativos),sum(positivos)))
