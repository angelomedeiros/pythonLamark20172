import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Pdf import GerarPdf

def enviarEmail(dicionario):
    try:
        smtp_server = 'smtp-mail.outlook.com' # Substitua pelo smtp de hospedagem do seu email
        smtp_port = 587 # Substitua pela porta do smtp de hospedagem do seu email
        acc_addr = 'seu@email.com' # Substitua pelo seu email
        acc_pwd = 'suaSenha' # Senha do email

        to_addr = 'destinatario@email.com' # Altere o destinatário
        subject = 'Assunto' # Altere o assunto
        body = 'Conteudo' # Altere o conteúdo

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(acc_addr, acc_pwd)

        msg = MIMEMultipart()
        msg["From"] = acc_addr
        msg["To"] = to_addr
        msg["Subject"] = subject

        with open(GerarPdf.pdf(dicionario), 'rb') as f:
            msgImg = MIMEApplication(f.read(), name=GerarPdf.pdf(dicionario))
        msg.attach(msgImg)

        msgText = MIMEText('<b>{}</b><br><img src="cid:{}"><br>'.format(body, GerarPdf.pdf(dicionario)), 'html')
        msg.attach(msgText)

        server.sendmail(acc_addr, to_addr, msg.as_string())
        server.quit()

        print("\nEmail enviado com sucesso!")

    except:
        print("\nNão foi possível enviar o email!")
