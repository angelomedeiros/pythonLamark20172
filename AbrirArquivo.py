convidados = open("convidados.txt","r")
















w,y = [],[]

for i in range(11):
    w.append(convidados.readline().split())

w.pop(0)

for j in w:
    y.append(j[0].split("-"))
    y.append(j[1].split("-"))

dicionario = {}

for key,value in y:
    dicionario[key] = value

print(dicionario)

convidados.close()