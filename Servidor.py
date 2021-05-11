from flask import Flask, jsonify, request
from funcs import *
from lendoEtiqueta import lerEtiqueta
from peewee import *
from Dados import Dado
from Dados import User
from playhouse.shortcuts import dict_to_model
import os



app = Flask("Server Smart Storage")


for d in Dado.select():
    print("Nome:  ")
    print(d.nome)

@app.route("/compras", methods = ['POST'])
def retornaCompras():
    
    compras = 0
    
    userSlot = []
    
    addCompras = 1
    
    body = request.get_json()
    
    nome = novoComparar(body["nome"])
    
    for u in User.select():
        print(u.usuario)
        if(u.usuario == body["nome"]):
            compras = 1 + compras
            userSlot.append(u.id)
    
                 
    return {"status:": 200 ,"Usuario": nome, "Quantidade de produtos": compras, "Slots": userSlot}



@app.route("/cadastro", methods = ['POST'])
def cadastraUsuarios():
    
    body = request.get_json()
    
    usuarioAPP = novoUsuario(body["nome"], body["email"], body["senha"])
    
    return {"status:": 200 ,"dados": usuarioAPP}

@app.route("/dados", methods = ['POST'])
def recebeDados():
    
    body = request.get_json()
    
    dado = novoDado(body["nome"], body["endereco"], body["bloco"], body["ap"], body["email"])
    
    Dado.create(nome = dado.get("nome"), endereco = dado.get("endereco"), bloco = dado.get("bloco"), ap = dado.get("ap"), email = dado.get("email"))
    
    return {"status:": 200, "informações de entrega": dado}

@app.route("/enviar", methods = ['Get'])
def enviaDados():
    
    body = request.get_json()
    
    receber  = body["imagem"] 
    
    ok = "OK!"
    
    usuario = lerEtiqueta(receber)
    
    User.create(usuario = usuario, img = (receber))
    
    return {"status:": 200, "Encomenda de":usuario, "Status da Entrega": ok}

@app.route("/excluir", methods = ['Post'])
def excluiDados():
    
    body = request.get_json()
    
    receber  = body["id"]
    
    usuario = ""
    
    msg = "OK!"
    
    key = False
    
    for u in User.select():
        if(u.id == int(receber)):
            usuario = u.usuario
    
    
    for u in User.select():
        if(u.id == int(receber)):
            u.delete_instance()
    
    if(not usuario):
        msg  = "Não alterado"
        usuario = "Usuário não encontrado"
            
    
    
    
    
    return {"status:": 200, "Encomenda de":usuario, "Situação de exclusão do slot": msg}


app.run()