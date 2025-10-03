import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação Tkinter")
root.geometry("800x650")
root.resizable(False,False)

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

F1foi = True

def F1(event):
    global F1foi
    if(F1foi):
        F1foi = False
        global janela_Item
        janela_Item = tk.Toplevel(root)
        janela_Item.title("Novo Item")
        janela_Item.geometry("450x300")
        janela_Item.resizable(False,False)
        janela_Item.protocol("WM_DELETE_WINDOW",F1n)
        imagem = tk.PhotoImage(file="ibagens/batata.gif")
        labelitem = tk.Label(janela_Item, image=imagem, width=182, height=125, border=1, relief="solid").place(x=20,y=20)


def F1n():
    global F1foi
    F1foi = True
    janela_Item.destroy()

F3foi = True

def F3(event):
    global F3foi
    if(F3foi):
       F3foi = False
       global janela_preco
       janela_preco = tk.Toplevel(root)
       janela_preco.title("Consultar preco")
       janela_preco.geometry("300x150")
       janela_preco.protocol("WM_DELETE_WINDOW",F3n)

def F3n():
    global F3foi
    F3foi = True
    janela_preco.destroy()



#linha 1
Subcaixa = tk.Entry(root, textvariable=SubValor, width=12, font=("Arial", 20, ""), state="disabled").place(x=col1,y=(40 + (4.1 * 0)))
descaixa = tk.Entry(root, textvariable=DesValor, width=12, font=("Arial", 20, ""), state="disabled").place(x=col2,y=(40 + (4.1 * 0)))

label = tk.Label(root, text="Sub-Total").place(x=col1,y=(40 + (4.1 * 0)) - 25)
label = tk.Label(root, text="Desconto").place(x=col2,y=(40 + (4.1 * 0)) - 25)

#linha 2
tocaixa = tk.Entry(root, textvariable=TotalValor, width=24, font=("Arial", 25, ""), state="disabled").place(x=col1,y=(40 * (4.1 * 1)) + 15)
label = tk.Label(root, text="Total").place(x=col1,y=(40 * (4.1 * 1))- 10)

#linha 3
Resotao = tk.Entry(root, textvariable=ResValor, width=12, font=("Arial", 20, "")).place(x=col1,y=(40 * (4.1 * 2)))
Trobotao = tk.Entry(root, textvariable=TroValor, width=12, font=("Arial", 20, ""), state="disabled").place(x=col2,y=(40 * (4.1 * 2)))

label = tk.Label(root, text="Valor Recebido").place(x=col1,y=(40 * (4.1 * 2)) - 25)
label = tk.Label(root, text="Troco").place(x=col2,y=(40 * (4.1 * 2))- 25)

#linha 4
opcoes = ["Débito", "Crédito", "Dinheiro", "Voucher", "Cartão Presente", "Pix"]
combo = ttk.Combobox(root, values=opcoes, width=27).place(x=col1,y=410)
label = tk.Label(root, text="Formas de Pagamento").place(x=col1,y=385)

#o famoso listbox
global listbox
listbox = tk.Listbox(root, height=20, width=50, listvariable=PayValor).place(x=10,y=40)
label = tk.Label(root, text="Lista de Produtos").place(x=110,y=10)

#imagem produto
global imagem
imagem = tk.PhotoImage(file="ibagens/batata.gif")
imagem = imagem.subsample(4,4)
label = tk.Label(root, image=imagem, width=182, height=125, border=1, relief="solid").place(x=600,y=370)

#imagem empresa
global imagemlogo
imagemlogo = tk.PhotoImage(file="ibagens/logi.png")
imagemlogo = imagemlogo.subsample(4,4)
label = tk.Label(root, image=imagemlogo, width=300, height=200).place(x=10,y=400)

#codigo de barras
label = tk.Label(root, text="Código de rabas").place(x=col1,y=450)
label = tk.Label(root, text="01100101010010110101011001").place(x=col1,y=480)

label = tk.Label(root, text="F1 - Novo Item").place(x=col2,y=500)
label = tk.Label(root, text="F2 - Remover Item").place(x=col2,y=520)
label = tk.Label(root, text="F3 - Consultar Preco").place(x=col2,y=540)
label = tk.Label(root, text="F4 - Imprimir/Concluir Compra").place(x=col2,y=560)
label = tk.Label(root, text="F5 - Adicionar Produto").place(x=col2,y=580)
label = tk.Label(root, text="F12 - Nova Compra").place(x=col2,y=600)

root.bind("<F1>", F1)


root.mainloop()