import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviarEmail():
    try:
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        acc_addr = 'angelo-bartira@hotmail.com'
        acc_pwd = 'ANGELO&BARTIRA'

        to_addr = 'angelomedeiros3@gmail.com'
        subject = 'Contatos - Equipe [Angelo e Bartira]'
        body = 'Segue os contatos em anexo.'

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(acc_addr, acc_pwd)

        msg = MIMEMultipart()
        msg["From"] = acc_addr
        msg["To"] = to_addr
        msg["Subject"] = subject

        pdfname='NumerosTelefone.pdf'
        with open('NumerosTelefone.pdf', 'rb') as f:
            msgImg = MIMEApplication(f.read(), name=pdfname)
        msg.attach(msgImg)

        msgText = MIMEText('<b>{}</b><br><img src="cid:{}"><br>'.format(body, pdfname), 'html')
        msg.attach(msgText)

        server.sendmail(acc_addr, to_addr, msg.as_string())
        server.quit()

        print("\nEmail enviado com sucesso!")

    except:
        print("\nNão foi possível enviar o email!")