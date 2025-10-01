import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação Tkinter")
root.geometry("800x600")

col1 = 350
col2 = 600
col3 = 200
col4 = 200

SubValor = tk.StringVar()
DesValor = tk.StringVar()
ResValor = tk.StringVar()
TotalValor = tk.StringVar()
TroValor = tk.StringVar()
PayValor = tk.StringVar()

#linha 1
Subotao = tk.Entry(root, textvariable=SubValor, width=12, font=("Arial", 20, "")).place(x=col1,y=(40 + (4.1 * 0)))
desbotao = tk.Entry(root, textvariable=DesValor, width=12, font=("Arial", 20, "")).place(x=col2,y=(40 + (4.1 * 0)))

label = tk.Label(root, text="Sub-Total").place(x=col1,y=(40 + (4.1 * 0)) - 25)
label = tk.Label(root, text="Desconto").place(x=col2,y=(40 + (4.1 * 0)) - 25)

#linha 2
tobotao = tk.Entry(root, textvariable=TotalValor, width=24, font=("Arial", 25, "")).place(x=col1,y=(40 * (4.1 * 1)) + 15)
label = tk.Label(root, text="Total").place(x=col1,y=(40 * (4.1 * 1))- 10)

#linha 3
Subotao = tk.Entry(root, textvariable=ResValor, width=12, font=("Arial", 20, "")).place(x=col1,y=(40 * (4.1 * 2)))
desbotao = tk.Entry(root, textvariable=TroValor, width=12, font=("Arial", 20, "")).place(x=col2,y=(40 * (4.1 * 2)))

label = tk.Label(root, text="Valor Recebido").place(x=col1,y=(40 * (4.1 * 2)) - 25)
label = tk.Label(root, text="Troco").place(x=col2,y=(40 * (4.1 * 2))- 25)

#linha 4
opcoes = ["Débito", "Crédito", "Dinheiro", "Voucher", "Cartão Presente", "Pix"]
combo = ttk.Combobox(root, values=opcoes, width=27).place(x=col1,y=410)
label = tk.Label(root, text="Formas de Pagamento").place(x=col1,y=385)


#o famoso listbox
listbox = tk.Listbox(root, height=20, width=50, listvariable=PayValor).place(x=10,y=40)
label = tk.Label(root, text="Lista de Produtos").place(x=110,y=10)

#imagem produto
imagem = tk.PhotoImage(file="ibagens/batata.gif")
imagem = imagem.subsample(4,4)
label = tk.Label(root, image=imagem, width=200, height=100).place(x=580,y=380)

#imagem empresa
imagemlogo = tk.PhotoImage(file="ibagens/logi.png")
imagemlogo = imagemlogo.subsample(4,4)
label = tk.Label(root, image=imagemlogo, width=300, height=200).place(x=10,y=380)



root.mainloop()