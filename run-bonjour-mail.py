# send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os
import requests
from io import BytesIO

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('GMAIL_PASSWORD')
gmail_receiver = os.getenv('GMAIL_RECEIVER')

# Função para obter uma imagem de gato aleatória da API
def obter_imagem_gato():
    url = 'https://api.thecatapi.com/v1/images/search'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados[0]['url']

# Configuração do email
de = gmail_user
para = gmail_receiver
assunto = 'Abra para começar bem o seu dia'
url_imagem = obter_imagem_gato()
corpo = f'''
<html>
  <body>
    <p>Bom dia, princesa 🌹<br></p>
    <p>Toma esse gatinho pra começar o seu dia bem 🐈❤️<br>
       <img src="{url_imagem}" alt="Gato" width="600"/></p>
  </body>
</html>
'''

# Cria a mensagem MIME
mensagem = MIMEMultipart('alternative')
mensagem['From'] = de
mensagem['To'] = para
mensagem['Subject'] = assunto

# Adiciona o corpo do e-mail em formato HTML
mensagem.attach(MIMEText(corpo, 'html'))

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
