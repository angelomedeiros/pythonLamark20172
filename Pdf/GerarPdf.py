from reportlab.pdfgen import canvas

def pdf(dicionario):
    pdfName = "NumerosTelefone.pdf"
    c = canvas.Canvas(pdfName)

    c.setFont('Times-Bold', 12) # Configura a fonte para negrito
    c.drawString(100, 780, "Nomes e telefones") # Título do conteúdo do PDF
    c.setFont('Times-Roman', 12)  # Configura a fonte para o normal

    h0 = 750 # Altura inicial da lista menos 30 unidades

    for key, value in dicionario.items():
        nomeTelefone = "{}: {}".format(str(key), str(value))
        c.drawString(100, h0, nomeTelefone)
        h0 -= 15 # Distância entrelinha

    c.save() # Salva documento

    return pdfName