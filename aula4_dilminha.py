sim,nao = 0,0

for i in range(15):
    voto = int(input("Dilma tá reeleita(1 para sim / 2 para não)? "))
    if voto == 1:
        sim += 1
    else:
        nao += 1

print("Votos sim: %d" % sim)
print("Votos não: %d" % nao)
