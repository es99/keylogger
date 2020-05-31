#!/usr/local/bin/python3
# coding: utf-8

import smtplib
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Gera a data atual num formato amigável para o usuário ex: 30/05/2020 - 10:45
data = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")

#username e senha para logar no servidor
mail_origem = "dunmorelouie58@gmail.com"
password = '62sURSoGbt'

#Conta de Email de destino
mail_destino = "kidle_windows@yahoo.com"

#Conexão com o servidor SMTP do Google
smtp_server = "smtp.gmail.com"
port = 587

#Função que faz o envio da mensagem
def enviaEmail():
  try:
    smtpObj = smtplib.SMTP(smtp_server, port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail_origem, password)
    smtpObj.sendmail(mail_origem, mail_destino, text)
  except Exception as e:
    print(e)
  finally:
    smtpObj.quit()

message = MIMEMultipart()
message["Subject"] = "Email com anexo"
message["From"] = mail_origem
message["To"] = mail_destino

filename = "logger.txt"

with open('corpo_msg.txt', 'r') as file:
  text = file.read()

message.attach(MIMEText(text, "plain"))

with open(filename, 'rb') as anexo:
  part = MIMEBase("application", "octet-stream")
  part.set_payload(anexo.read())

#Encode file in ASCII to send email
encoders.encode_base64(part)

#ADD Header, uma tupla que retorna chave/valor
part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

message.attach(part)
text = message.as_string()

#Chamada da função
enviaEmail()
