from reportlab.pdfgen import canvas

def pdf(dicionario):
    c = canvas.Canvas("NumerosTelefone.pdf")

    c.setFont('Times-Bold', 12) # Configura a fonte para negrito
    c.drawString(100, 780, "Nomes e telefones")
    h0 = 750 # Altura inicial da lista menos 30 unidades
    c.setFont('Times-Roman', 12) # Configura a fonte para o normal

    for key, value in dicionario.items():
        nomeTelefone = "{}: {}".format(str(key), str(value))
        c.drawString(100, h0, nomeTelefone)
        h0 -= 15

    c.save()