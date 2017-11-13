w, y, dicionario = [], [], {}

def dicionarioConvidados(dados):
    for i in range(11):
        w.append(dados.readline().split())  # Cria array fatiando nos espaços
    w.pop(0)  # Exclui a primeira linha do convidados.txt

    for j in w:
        y.append(j[0].split("-"))  # Cria array fatiando nos "menos"
        y.append(j[1].split("-"))

    for key, value in y:
        dicionario[key] = value  # Cria o dicionário

    return dicionario