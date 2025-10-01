import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação Tkinter")
root.geometry("800x600")

def exemplo():
    label.config(text="Botão clicado!")

col1 = 350
col2 = 600
col3 = 200
col4 = 200
SubValor = 0
DesValor = 0
button = tk.Entry(root, textvariable=SubValor).place(x=col1,y=35)
button = tk.Entry(root, textvariable=DesValor).place(x=col2,y=35)
label = tk.Label(root, text="Sub-Total").place(x=col1,y=10)
label = tk.Label(root, text="Desconto").place(x=col2,y=10)
listbox = tk.Listbox(root, height=20, width=50).place(x=10,y=10)

root.mainloop()