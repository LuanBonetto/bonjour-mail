# send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
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
assunto = 'Bom dia - teste'
corpo = (
    'Bom dia princesa!\n'
    'Espero que tenha um ótimo dia 🌹\n'
    'Toma esse gatinho pra alegrar seu dia!\n\n'
)

# Obtendo a URL da imagem de gato
url_imagem = obter_imagem_gato()
imagem_resposta = requests.get(url_imagem)
imagem_bytes = BytesIO(imagem_resposta.content)

# Cria a mensagem MIME
mensagem = MIMEMultipart()
mensagem['From'] = de
mensagem['To'] = para
mensagem['Subject'] = assunto

# Adiciona o corpo do e-mail
mensagem.attach(MIMEText(corpo, 'plain'))

# Adiciona a imagem de gato como anexo
imagem = MIMEImage(imagem_bytes.read())
imagem.add_header('Content-Disposition', 'attachment', filename='gato.jpg')
mensagem.attach(imagem)

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
