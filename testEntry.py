from tkinter import *


root = Tk()

prompt = Label(root, text="Insere algo")
prompt.pack(side="left")

entry = Entry(root)
entry.pack(side="left")


def on_key_pressing(event, entry, label):
    print(entry.get(), label.cget("text"))
    if entry.get() != label.cget("text"):
        label.config(text=entry.get())

# Associando o evento <Key> com a chamada
# a funcão on_key_pressing
entry.bind("<KeyRelease>", lambda e: on_key_pressing(e, entry, label))

label = Label(root, text="")
label.pack(side="left")

root.mainloop()