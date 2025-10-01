import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação Tkinter")
root.geometry("800x600")

def exemplo():
    label.config(text="Botão clicado!")

button = tk.Button(root, text="Selecionar Item").place(x=500,y=30)
label = tk.Label(root, text="Bem-vindo à minha aplicação!").place(x=500,y=10)
listbox = tk.Listbox(root, height=20, width=50).place(x=10,y=10)

root.mainloop()