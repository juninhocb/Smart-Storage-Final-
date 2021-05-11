import tkinter as tk
root = tk.Tk()

imagem = tk.PhotoImage(file="Camisa.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.place(relx = 0.5, rely = 0.3, height = 130, width = 180)

root.mainloop()

