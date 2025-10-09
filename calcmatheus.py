import tkinter as tk
from tkinter import PhotoImage, ttk

root = tk.Tk()
root.title("Minha Aplicação Tkinter")
root.geometry("800x650")
root.resizable(False,False)

col1 = 350
col2 = 600
col3 = 200
col4 = 200

global SubValor
global DesValor
global ResValor
global TotalValor
global TroValor
global PayValor

SubValor = tk.StringVar()
SubValor.set(0.0)
DesValor = tk.StringVar()
DesValor.set(0.0)
ResValor = tk.StringVar()
ResValor.set(0.0)
TotalValor = tk.StringVar()
TotalValor.set(0.0)
TroValor = tk.StringVar()
TroValor.set(0.0)

F1foi = True

def F1(event):
    global F1foi
    if(F1foi):
        F1foi = False
        global janela_Item
        global imagems
        global codigo
        global qtde
        global labelitem
        global labelpreco
        global barrasqtde
        global barrascaixa
        qtde = tk.StringVar()
        codigo = tk.StringVar()
        janela_Item = tk.Toplevel(root)
        janela_Item.title("Novo Item")
        janela_Item.geometry("450x300")
        janela_Item.resizable(False,False)
        janela_Item.protocol("WM_DELETE_WINDOW",F1n)
        imagems = PhotoImage(file="")
        labelitem = tk.Label(janela_Item, image=imagems, width=182, height=125, border=1, relief="solid")
        labelitem.place(x=20,y=20)
        labelpreco = tk.Label(janela_Item, border=1, text="Preço Unitário: ")
        labelpreco.place(x=220,y=20)
        barrascaixa = tk.Entry(janela_Item, textvariable=codigo, width=12, font=("Arial", 20, ""))
        barrasqtde = tk.Entry(janela_Item, textvariable=qtde, width=12, font=("Arial", 20, ""))
        barrascaixa.place(x=20,y=150)
        barrasqtde.place(x=220,y=150)
        barrascaixa.bind("<Return>", lambda event: F1enter(codigo.get()))
        barrasqtde.bind("<Return>", enviar)
        tk.Label(janela_Item, border=1, text="Inserir codigo de barras").place(x=20,y=190)
        tk.Label(janela_Item, border=1, text="Inserir quantidade").place(x=220,y=190)
        barrascaixa.focus()

def F1enter(valor):
    global valors
    valors = 0
    global imagems
    global nome
    if valor == "01":
        nome = "batata_kg"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 10
    elif valor == "00":
        nome = "televisao"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 1050
    elif valor == "10":
        nome = "arroz_kg"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 15
    elif valor == "11":
        nome = "feijao_kg"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 13
    labelpreco.config(text=f"Preço Unitário: {valors}")
    labelitem.config(image=imagems)
    barrasqtde.focus()

def enviar(event):
    if(str(codigo.get()) != "" and str(qtde.get()) != ""):
        global F1foi
        listbox.insert(tk.END, f"{codigo.get()}                 {nome}                 {qtde.get()}                 {valors}.00")
        AtualizarPreco(event=event)
        F1foi = True
        janela_Item.destroy()
    
def selection(event):
    selec = listbox.curselection()
    if(selec):
        peguei = str(listbox.get(selec))
        nah = peguei.split("                 ")
        imagems = tk.PhotoImage(file=f"ibagens/{nah[1]}.png").subsample(4,4)
        labelimagem.config(image=imagems)
        labelimagem.image = imagems
        labelbarras.config(text=f"510000{nah[0]}7")

def F1n():
    global F1foi
    F1foi = True
    janela_Item.destroy()

F3foi = True

def F2(event):
    opa = listbox.curselection()
    if(opa):
        listbox.delete(opa)
        AtualizarPreco(event=event)

def AtualizarPreco(event):
    valores = 0
    i = 0
    while(i < listbox.size()):
        selec = str(listbox.get(i))
        nah = selec.split("                 ")
        valores += float(nah[2]) * float(nah[3])
        SubValor.set(valores)
        i+= 1
    if(listbox.size() == 0):
        SubValor.set("0.00")
    TotalValor.set(float(SubValor.get()) - float(DesValor.get()))

def CalcularTroco(event):
    if(ResValor.get() == ""):
        ResValor.set("0.00")
    troco = float(TotalValor.get()) - float(ResValor.get())
    TroValor.set(float(troco * -1))
    if(TroValor.get() == "-0.0"):
        TroValor.set("0.0")

def mudapagamento(event):
    if(combo.get() == "Débito" or combo.get() == "Crédito" or combo.get() == "Pix"):
        ResValor.set(float(TotalValor.get()))
    else:
        ResValor.set("")
    CalcularTroco(event=event)

def F3(event):
    janela_Item = tk.Toplevel(root)
    janela_Item.title("Consultar Produtos")
    janela_Item.geometry("450x300")
    janela_Item.resizable(False,False)

global Subcaixa
global Descaixa
global Rescaixa
global Trocaixa

#linha 1
Subcaixa = tk.Entry(root, textvariable=SubValor, width=12, font=("Arial", 20, ""), state="disabled")
descaixa = tk.Entry(root, textvariable=DesValor, width=12, font=("Arial", 20, ""), state="disabled")

Subcaixa.place(x=col1,y=(40 + (4.1 * 0)))
descaixa.place(x=col2,y=(40 + (4.1 * 0)))

label = tk.Label(root, text="Sub-Total").place(x=col1,y=(40 + (4.1 * 0)) - 25)
label = tk.Label(root, text="Desconto").place(x=col2,y=(40 + (4.1 * 0)) - 25)

#linha 2
tocaixa = tk.Entry(root, textvariable=TotalValor, width=24, font=("Arial", 25, ""), state="disabled").place(x=col1,y=(40 * (4.1 * 1)) + 15)
label = tk.Label(root, text="Total").place(x=col1,y=(40 * (4.1 * 1))- 10)

#linha 3
Resotao = tk.Entry(root, textvariable=ResValor, width=12, font=("Arial", 20, ""))
Resotao.place(x=col1,y=(40 * (4.1 * 2)))
Resotao.bind("<Return>", CalcularTroco)
Trobotao = tk.Entry(root, textvariable=TroValor, width=12, font=("Arial", 20, ""), state="disabled").place(x=col2,y=(40 * (4.1 * 2)))

label = tk.Label(root, text="Valor Recebido").place(x=col1,y=(40 * (4.1 * 2)) - 25)
label = tk.Label(root, text="Troco").place(x=col2,y=(40 * (4.1 * 2))- 25)

#linha 4
global opcoes
opcoes = ["Débito", "Crédito", "Dinheiro", "Voucher", "Pix"]
combo = ttk.Combobox(root, values=opcoes, width=27, state="readonly")
combo.place(x=col1,y=410)
combo.bind("<<ComboboxSelected>>",mudapagamento)
label = tk.Label(root, text="Formas de Pagamento").place(x=col1,y=385)

#o famoso listbox
global listbox
listbox = tk.Listbox(root, height=20, width=50)
listbox.place(x=10,y=40)
listbox.bind("<ButtonRelease-1>", selection)
label = tk.Label(root, text="Lista de Produtos").place(x=110,y=10)

#imagem produto
global imagem
global labelimagem
imagem = PhotoImage(file="").subsample(3,3)
labelimagem = tk.Label(root, image=imagem, width=182, height=125, border=1, relief="solid")
labelimagem.place(x=600,y=370)

#imagem empresa
global imagemlogo
imagemlogo = tk.PhotoImage(file="ibagens/logi.png")
imagemlogo = imagemlogo.subsample(3,3)
label = tk.Label(root, image=imagemlogo, width=300, height=200).place(x=10,y=400)

#codigo de barras
label = tk.Label(root, text="Código de rabas").place(x=col1,y=450)
global labelbarras
labelbarras = tk.Label(root, text="01100101010010110101011001")
labelbarras.place(x=col1,y=480)

label = tk.Label(root, text="F1 - Novo Item").place(x=col2,y=500)
label = tk.Label(root, text="F2 - Remover Item").place(x=col2,y=520)
label = tk.Label(root, text="F3 - Consultar Preco").place(x=col2,y=540)
label = tk.Label(root, text="F4 - Imprimir/Concluir Compra").place(x=col2,y=560)
label = tk.Label(root, text="F12 - Nova Compra").place(x=col2,y=580)

root.bind("<F1>", F1)
root.bind("<F2>", F2)
root.bind("<F3>", F3)

root.mainloop()