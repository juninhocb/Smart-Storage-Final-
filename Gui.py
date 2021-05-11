from tkinter import *
from tkinter import ttk
from Gui1 import *



root = Tk()
root.tittle = ("Projeto Integrador Grupo C")
root.geometry('800x350')
root.resizable (False,False)


class Application (Gui1): 
    
    def __init__(self):
        self.root = root
        self.showMain()
        root.mainloop()
        

   
Application()