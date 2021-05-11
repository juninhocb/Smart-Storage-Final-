# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:09:53 2021

@author: dscal
"""

import smtplib, ssl

def enviarEmail(email):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "smartstorageserver@gmail.com"
    receiver_email = email
    password = "Smart12345"
    message = """\
Subject: Tem encomenda para voce

Essa e uma mensagem automatizada do sistema SmartStorage para avisar que voce recebeu uma encomenda.

Verifique no aplicativo SmartStorage o compartimento que ela este armazenada

Atenciosamente,
Equipe SmartStorage"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)