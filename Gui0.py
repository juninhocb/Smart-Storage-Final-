from tkinter import *
import os
from Dados import Dado


class Gui1():
   
    def pegaVariavel(self):
        
        self.frame1 = Frame(self.root, bg = '#F8F8FF')
        self.frame1.place(relx = 0.025, rely = 0.025, relwidth = 0.95, relheight = 0.95)
        
        self.lb_projetos = Label(self.frame1, text = "Smart Storage - Receptor de Encomendas"
                                 , font = ('verdana', 15, 'bold'), bg = '#F8F8FF')
        
        self.entryName = Entry(self.frame1, textvariable="teste conteudo")
        self.entryName.place(relx = 0.027, rely = 0.30, height = 30, width = 250)
        
        self.btOk = Button(self.frame1, text = "Carregar Dados",bg = "grey", command=lambda: self.frame1.destroy
                           , font = ('verdana', 12, 'bold'))
        self.btOk.place(relx = 0.20  , rely = 0.8, relwidth = 0.40, relheight = 0.075)