# send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('GMAIL_PASSWORD')
gmail_receiver = os.getenv('GMAIL_RECEIVER')

# Configuração do email
de = gmail_user
para = gmail_receiver
assunto = 'Bom dia - teste'
corpo = 'Bom dia princesa! \n Espero que tenha um ótimo dia 🌹 \n Esse é só um teste, me avise se recebeu.'

# Cria a mensagem MIME
mensagem = MIMEMultipart()
mensagem['From'] = de
mensagem['To'] = para
mensagem['Subject'] = assunto
mensagem.attach(MIMEText(corpo, 'plain'))

try:
    # Conectando ao servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Inicia a conexão segura
    server.login(gmail_user, gmail_password)
    
    # Envia o email
    texto = mensagem.as_string()
    server.sendmail(de, para, texto)
    print('Email enviado com sucesso!')
    
except Exception as e:
    print(f'Ocorreu um erro: {e}')
    
finally:
    server.quit()  # Finaliza a conexão com o servidor
