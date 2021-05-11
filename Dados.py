from peewee import *
import os

arq = './Dado.DB'
DB = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = DB


class Dado(BaseModel):
    nome = CharField()
    endereco = CharField()
    bloco = CharField()
    ap = IntegerField()
    email = CharField()

class User(BaseModel):
    id = ForeignKeyField
    usuario = CharField()
    img = CharField()
    

    
   
   


if __name__ == "__main__":  # se estiver rodando esse programa, executa!  (evita rodar no import)


    if os.path.exists(arq):
        os.remove(arq)
   
    try:
        DB.connect()
        DB.create_tables([Dado, User])
    except OperationalError as e:
        print('erro ao criar tabela:' +str(e))

#dado1 = Dado.create(nome = 'Marcela',endereco = 'Rua Tal numero tal', bloco = 'C', ap = '110', img = 'Etiqueta2.png', email = 'jj@hotmail.com')
        
#User.create(usuario = 'Marcela',img = 'Etiqueta2.png')
'''
for d in Dado.select():
    print("Nome:  ")
    print(d.nome)

'''


