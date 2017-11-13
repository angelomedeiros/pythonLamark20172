w, y, dicionario = [], [], {}

def dicionarioConvidados(dados):

    for i in range(11):
        w.append(dados.readline().split())
    w.pop(0)

    for j in w:
        y.append(j[0].split("-"))
        y.append(j[1].split("-"))

    for key, value in y:
        dicionario[key] = value

    return dicionario
