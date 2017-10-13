listaEntrada = [int(input("Digite um número: ")) for i in range(6)]
listaFiltrada = list(filter(lambda x: x > 0, listaEntrada))
print(listaFiltrada)

