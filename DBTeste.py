from peewee import *
import os
from Dados import Dado


key = "Flávio Jefferson"

for d in Dado.select():
    if (d.nome == key):
        print(d.nome)
        print(d.endereco)
        print(d.bloco)
        print(d.ap)
        print(d.img)