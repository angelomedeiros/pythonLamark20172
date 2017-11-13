from Strings.AbrirArquivo import dicionarioConvidados
from Pdf import GerarPdf
from Email import EnviarEmail

# Armazena os dados na variável convidados
convidados = open("convidados.txt", "r")

# Retorna dicionário
dicionario = dicionarioConvidados(convidados)

# Gera o pdf
GerarPdf.pdf(dicionario)

# Imprime o dicionário na saída padrão
print("Dicionário com os contatos: {}".format(dicionario))

EnviarEmail.enviarEmail()

