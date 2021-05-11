from tkinter import *
import os
from Dados import Dado
from Dados import User
from SendEmail import enviarEmail

class Gui1():
   
    def showMain(self):
        self.c = 0
        
        self.email = ''
        
        ultimoUser = User.select().order_by(User.id.desc()).get()
        print(ultimoUser.usuario)
        print(ultimoUser.id)
        
        for u in User.select():
            print(u.usuario)
            print(u.id)
            print('\n')
                                    ### CRIÇÃO DA FRAME ###
        self.frame1 = Frame(self.root, bg = '#F8F8FF')
        self.frame1.place(relx = 0.025, rely = 0.025, relwidth = 0.95, relheight = 0.95)
        
                                    #### LOGO
        self.imagem = PhotoImage(file= 'logo.png')
        self.w = Label(self.frame1, image = self.imagem, bg = '#F8F8FF')
        self.w.imagem = self.imagem
        self.w.place(relx = 0.84, rely = 0.025, height = 115, width = 115)
                                    # FIM LOGO ##
        
        
        
                                    ### LABELS ###
        self.lb_projetos = Label(self.frame1, text = "Smart Storage - Receptor de Encomendas"
                                 , font = ('verdana', 15, 'bold'), bg = '#F8F8FF')
        self.lb_projetos.place(relx = 0.025, rely = 0.025)
        
        self.lb_Nome = Label(self.frame1, text = "Os dados do favorecido serão exibidos nos campos abaixo!"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.15)
        
        self.lb_Nome = Label(self.frame1, text = "Nome"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.24)
        
        self.lb_Nome = Label(self.frame1, text = "Endereço"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.42)
        
        self.lb_Nome = Label(self.frame1, text = "Bloco"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.025, rely = 0.60)
        
        self.lb_Nome = Label(self.frame1, text = "AP"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.20, rely = 0.60)
        
        self.lb_Nome = Label(self.frame1, text = "A última encomenda lida será carregada, clique em Atualizar!"
                                 , font = ('verdana', 10, 'bold'), bg = '#F8F8FF')
        self.lb_Nome.place(relx = 0.027, rely = 0.78)
        
                                    ### Entry ###
        
        self.entryName = Entry(self.frame1, textvariable="teste conteudo")
        self.entryName.place(relx = 0.027, rely = 0.30, height = 30, width = 250)
        
        self.entryEnd = Entry(self.frame1)
        self.entryEnd.place(relx = 0.027, rely = 0.48, height = 30, width = 250)
        
        self.entryBloco = Entry(self.frame1)
        self.entryBloco.place(relx = 0.027, rely = 0.67, height = 30, width = 115)
        
        self.entryAp = Entry(self.frame1)
        self.entryAp.place(relx = 0.20, rely = 0.67, height = 30, width = 115)
        
        self.entryNomeKey = Entry(self.frame1)
        self.entryNomeKey.place(relx = 0.027, rely = 0.87, height = 30, width = 200)
        
        self.entryNomeKey.insert(0, ultimoUser.usuario)
        
        for d in Dado.select():
            if (d.nome == ultimoUser.usuario):
                self.nome = d.nome
                self.endereco = d.endereco
                self.bloco = d.bloco
                self.ap = d.ap
                self.email = d.email
                self.c = self.c + 1
                
                self.entryName.delete(0,"end")
                self.entryName.insert(0, d.nome)
    
                self.entryEnd.delete(0,"end")
                self.entryEnd.insert(0, d.endereco)
    
                self.entryBloco.delete(0,"end")
                self.entryBloco.insert(0, d.bloco)
    
                self.entryAp.delete(0,"end")
                self.entryAp.insert(0, d.ap)
        
        for u in User.select():
            if (u.usuario == ultimoUser.usuario):
                self.img = u.img
    
    
        if(self.img):
            self.imagem = PhotoImage(file= self.img)
            self.w = Label(self.frame1, image = self.imagem)
            self.w.imagem = self.imagem
            self.w.place(relx = 0.37, rely = 0.3, height = 150, width = 350)
        else:
            print("ok")
            self.imagem = PhotoImage(file= "ProdutoS.png")
            self.w = Label(self.frame1, image = self.imagem)
            self.w.imagem = self.imagem
            self.w.place(relx = 0.37, rely = 0.3, height = 150, width = 350)
        
                                                   ###  Botões###
        
        self.btOk = Button(self.frame1, text = "Atualizar ",bg = "grey", command=lambda:self.showMain()
                                , font = ('verdana', 12, 'bold'))
        self.btOk.place(relx = 0.30  , rely = 0.87, relwidth = 0.15, relheight = 0.1)
        
        self.btOk = Button(self.frame1, text = "Alterar ",bg = "grey", command=lambda:changeData(self, self.entryNomeKey.get(), self.frame1
                                , self.entryName.get(), self.entryEnd.get(), self.entryBloco.get(), self.entryAp.get())
                                , font = ('verdana', 12, 'bold'))
        self.btOk.place(relx = 0.465 , rely = 0.87, relwidth = 0.15, relheight = 0.1)
        
        self.btOk = Button(self.frame1, text = "Confirmar Dados ",bg = "green", command=lambda:confirmDelivery(self, ultimoUser.usuario, self.email)
                                , font = ('verdana', 12, 'bold'))
        self.btOk.place(relx = 0.63 , rely = 0.87, relwidth = 0.20, relheight = 0.1)
        
                                                ### FIM BOTÕES ###
        
    
def changeData(self, key, frame1, nome, end, bloco, ap):
    
    outKey = False
    self.nome = nome
    self.endereco = end
    self.bloco = bloco
    self.ap = ap
    self.nomeKey = key

    for d in Dado.select():
        if (d.nome == self.nomeKey):
            d.endereco = self.endereco
            d.bloco = self.bloco
            d.ap = self.ap 
            d.save()
            outKey = True
        elif (outKey == False):
            self.nome = "não consta no banco de dados"
    
    
def confirmDelivery(self, key, email):
       
    outKey = False
    outKey2 = False
    self.deleteUser = key     
    '''
    for u in User.select():
        if (u.usuario == self.deleteUser and outKey2 == False):
            u.delete_instance()
            print('deletou')
            outKey = True
            outKey2 = True
        elif (outKey == False):
            self.nome = "não consta no banco de dados"
    '''
    
    messagebox.showinfo(title="Correto!", message= "Entrega confirmada com sucesso!", )
    
    self.entryName.delete(0,"end")
    self.entryName.insert(0, "")
    
    self.entryEnd.delete(0,"end")
    self.entryEnd.insert(0, "")
    
    self.entryBloco.delete(0,"end")
    self.entryBloco.insert(0, "")
    
    self.entryAp.delete(0,"end")
    self.entryAp.insert(0, "")
    
    self.entryNomeKey.delete(0,"end")
    self.entryNomeKey.insert(0, "")
    
    self.imagem = PhotoImage(file= "ProdutoS.png")
    self.w = Label(self.frame1, image = self.imagem)
    self.w.imagem = self.imagem
    self.w.place(relx = 0.37, rely = 0.3, height = 150, width = 350)
    
    enviarEmail(self.email)
    
            
        
        
        
        
         

   