import tkinter as tk
from tkinter import PhotoImage, ttk

root = tk.Tk()
root.title("Minha Aplicação Tkinter")
root.geometry("800x625")
root.resizable(False,False)
bgimage = PhotoImage(file="ibagens/Design sem nome.png")
tk.Label(root,image=bgimage, width=800, height=650).place(x=-2,y=-2)

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

    if valor == "001":
        nome = "batata_kg"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 2.80
        barrasqtde.focus()
    elif valor == "000":
        nome = "televisao"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 2559.90
        barrasqtde.focus()
    elif valor == "010":
        nome = "arroz_kg"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 4.90
        barrasqtde.focus()
    elif valor == "011":
        nome = "feijao_kg"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 7.90
        barrasqtde.focus()
    elif valor == "100":
        nome = "Coca350ML"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 6.50
        barrasqtde.focus()
    elif valor == "101":
        nome = "Pan_Seara"
        imagems = tk.PhotoImage(file=f"ibagens/{nome}.png").subsample(4,4)
        valors = 18.90
        barrasqtde.focus()
    labelpreco.config(text=f"Preço Unitário: {valors}")
    labelitem.config(image=imagems)


def temdesconto(quantia, nome, valor, event):
    if(nome == "arroz_kg" and float(quantia) >= 2):
        DesValor.set(round(float(DesValor.get()) + ((quantia*(valor/100)*6)), 2))
    if(nome == "batata_kg" and float(quantia) >= 1.5):
        DesValor.set(round(float(DesValor.get()) + ((quantia*(valor/100)*4)), 2))
    if(nome == "feijao_kg" and float(quantia) >= 2):
        DesValor.set(round(float(DesValor.get()) + ((quantia*(valor/100)*4)), 2))
    if(nome == "Coca350ML" and float(quantia) >= 4):
        DesValor.set(round(float(DesValor.get()) + ((quantia*(valor/100)*10)), 2))
    if(nome == "Pan_Seara" and float(quantia) >= 3):
        DesValor.set(round(float(DesValor.get()) + ((quantia*(valor/100)*24)), 2))
    AtualizarPreco(event=event)

def enviar(event):
    if(str(codigo.get()) != "" and str(qtde.get()) != ""):
        global F1foi
        atualizaprod(nome, event)
        listbox.insert(tk.END, f"{codigo.get()}                 {nome}                 {float(qtde.get())}                 {valors}")
        AtualizarPreco(event=event)
        F1foi = True
        temdesconto(float(qtde.get()), nome, valors, event=event)
        janela_Item.destroy()

def atualizaprod(nome, event):
    i = 0
    while(i < listbox.size()):
        selec = str(listbox.get(i))
        nah = selec.split("                 ")
        if(nah[1] == nome):
            listbox.delete(i, i)
            qtde.set(float(qtde.get()) + float(nah[2]))
        i+=1
    AtualizarPreco(event=event)
    
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
    DesValor.set("0.0")

def AtualizarPreco(event):
    valores = 0
    i = 0
    while(i < listbox.size()):
        selec = str(listbox.get(i))
        nah = selec.split("                 ")
        valores += float(nah[2]) * float(nah[3])
        SubValor.set(round(valores, 2))
        i+= 1
    if(listbox.size() == 0):
        SubValor.set("0.00")
    TotalValor.set(round(float(SubValor.get()) - float(DesValor.get()), 2))
    mudapagamento(event=event)

def CalcularTroco(event):
    if(ResValor.get() == ""):
        ResValor.set("0.00")
    troco = float(TotalValor.get()) - float(ResValor.get())
    TroValor.set(round(float(troco * -1), 2))
    if(TroValor.get() == "-0.0"):
        TroValor.set("0.0")

def mudapagamento(event):
    if(combo.get() == "Débito" or combo.get() == "Crédito" or combo.get() == "Pix"):
        ResValor.set(round(float(TotalValor.get()), 2))
    else:
        ResValor.set("")
    CalcularTroco(event=event)

global f3estado
f3estado = True

def F3(event):
    global f3estado
    global janela_Item
    if(f3estado):
        janela_Item = tk.Toplevel(root)
        janela_Item.title("Consultar Produtos")
        janela_Item.geometry("450x300")
        janela_Item.resizable(False,False)
        janela_Item.bind("<F3>", F3)
        tk.Label(janela_Item, text="Televisão       ").place(x=20,y=20)
        tk.Label(janela_Item, text="Batata          ").place(x=20,y=40)
        tk.Label(janela_Item, text="Arroz           ").place(x=20,y=60)
        tk.Label(janela_Item, text="Feijão          ").place(x=20,y=80)
        tk.Label(janela_Item, text="Coca_Cola_350ML ").place(x=20,y=100)
        tk.Label(janela_Item, text="Panelinhas_Seara").place(x=20,y=120)
        tk.Label(janela_Item, text="codigo: 000").place(x=200,y=20)
        tk.Label(janela_Item, text="codigo: 001").place(x=200,y=40)
        tk.Label(janela_Item, text="codigo: 010").place(x=200,y=60)
        tk.Label(janela_Item, text="codigo: 011").place(x=200,y=80)
        tk.Label(janela_Item, text="codigo: 100").place(x=200,y=100)
        tk.Label(janela_Item, text="codigo: 101").place(x=200,y=120)
        f3estado = not f3estado
    else:
        janela_Item.destroy()
        f3estado = not f3estado

global f5estado
f5estado = True

def F5(event):
    global f5estado
    global janela_promo
    if(f5estado):
        janela_promo = tk.Toplevel(root)
        janela_promo.title("Consultar Promoções")
        janela_promo.geometry("550x300")
        janela_promo.resizable(False,False)
        janela_promo.bind("<F5>", F5)
        tk.Label(janela_promo, text="Televisão       ").place(x=20,y=20)
        tk.Label(janela_promo, text="Batata          ").place(x=20,y=40)
        tk.Label(janela_promo, text="Arroz           ").place(x=20,y=60)
        tk.Label(janela_promo, text="Feijão          ").place(x=20,y=80)
        tk.Label(janela_promo, text="Coca_Cola_350ML ").place(x=20,y=100)
        tk.Label(janela_promo, text="Panelinhas_Seara").place(x=20,y=120)
        tk.Label(janela_promo, text="Não Possui").place(x=200,y=20)
        tk.Label(janela_promo, text="Na compra de 1.5Kg ou mais  > 4% de desconto").place(x=200,y=40)
        tk.Label(janela_promo, text="Na compra de 2 ou mais  > 6% de desconto").place(x=200,y=60)
        tk.Label(janela_promo, text="Na compra de 2 ou mais  > 4% de desconto").place(x=200,y=80)
        tk.Label(janela_promo, text="Na compra de 4 ou mais  > 10% de desconto").place(x=200,y=100)
        tk.Label(janela_promo, text="Na compra de 3 ou mais  > 24% de desconto").place(x=200,y=120)
        f5estado = not f5estado
    else:
        janela_promo.destroy()
        f5estado = not f5estado
    
def F4(event):
    janela_Result = tk.Toplevel(root)
    janela_Result.title("Consultar Produtos")
    janela_Result.geometry("400x100")
    janela_Result.resizable(False,False)
    tk.Label(janela_Result, text=f"Valor Total da Compra: {TotalValor.get()}").place(x=30,y=20)
    tk.Label(janela_Result, text=f"Valor Recebido da Compra: {ResValor.get()}").place(x=20,y=40)
    tk.Label(janela_Result, text=f"Troco: {TroValor.get()}").place(x=70,y=60)
    listbox.delete(0, tk.END)
    AtualizarPreco(event=event)

def F12(event):
    listbox.delete(0, tk.END)
    AtualizarPreco(event=event)

global Subcaixa
global Descaixa
global Rescaixa
global Trocaixa

#linha 1
Subcaixa = tk.Entry(root, textvariable=SubValor, width=12, font=("Arial", 20, ""), state="disabled")
descaixa = tk.Entry(root, textvariable=DesValor, width=12, font=("Arial", 20, ""), state="disabled")

Subcaixa.place(x=col1,y=(40 + (4.1 * 0)))
descaixa.place(x=col2,y=(40 + (4.1 * 0)))

label = tk.Label(root, text="Sub-Total", bg="white").place(x=col1,y=(40 + (4.1 * 0)) - 25)
label = tk.Label(root, text="Desconto", bg="white").place(x=col2,y=(40 + (4.1 * 0)) - 25)

#linha 2
tocaixa = tk.Entry(root, textvariable=TotalValor, width=24, font=("Arial", 25, ""), state="disabled").place(x=col1,y=(40 * (4.1 * 1)) + 15)
label = tk.Label(root, text="Total", bg="white").place(x=col1,y=(40 * (4.1 * 1))- 10)

#linha 3
Resotao = tk.Entry(root, textvariable=ResValor, width=12, font=("Arial", 20, ""))
Resotao.place(x=col1,y=(40 * (4.1 * 2)))
Resotao.bind("<Return>", CalcularTroco)
Trobotao = tk.Entry(root, textvariable=TroValor, width=12, font=("Arial", 20, ""), state="disabled", bg="white").place(x=col2,y=(40 * (4.1 * 2)))

label = tk.Label(root, text="Valor Recebido", bg="white").place(x=col1,y=(40 * (4.1 * 2)) - 25)
label = tk.Label(root, text="Troco", bg="white").place(x=col2,y=(40 * (4.1 * 2))- 25)

#linha 4
global opcoes
opcoes = ["Débito", "Crédito", "Dinheiro", "Voucher", "Pix"]
combo = ttk.Combobox(root, values=opcoes, width=27, state="readonly")
combo.place(x=col1,y=410)
combo.bind("<<ComboboxSelected>>",mudapagamento)
label = tk.Label(root, text="Formas de Pagamento", bg="white").place(x=col1,y=385)

#o famoso listbox
global listbox
listbox = tk.Listbox(root, height=20, width=50)
listbox.place(x=10,y=40)
listbox.bind("<ButtonRelease-1>", selection)
listbox.bind("<KeyRelease-Up>", selection)
listbox.bind("<KeyRelease-Down>", selection)
label = tk.Label(root, text="Lista de Produtos", bg="white").place(x=110,y=0)
iqua = 18
label = tk.Label(root, text="Código", bg="white").place(x=15,y=iqua)
label = tk.Label(root, text="Nome", bg="white").place(x=85,y=iqua)
label = tk.Label(root, text="Quantidade", bg="white").place(x=155,y=iqua)
label = tk.Label(root, text="Valor Unit.", bg="white").place(x=245,y=iqua)

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
label = tk.Label(root, text="Código de Barras", bg="white").place(x=col1,y=450)
global labelbarras
labelbarras = tk.Label(root, text="0", bg="white")
labelbarras.place(x=col1,y=480)

label = tk.Label(root, text="F1 - Novo Item", bg="white").place(x=col2,y=500)
label = tk.Label(root, text="F2 - Remover Item", bg="white").place(x=col2,y=520)
label = tk.Label(root, text="F3 - Consultar Preco", bg="white").place(x=col2,y=540)
label = tk.Label(root, text="F4 - Imprimir/Concluir Compra", bg="white").place(x=col2,y=560)
label = tk.Label(root, text="F5 - Promoções", bg="white").place(x=col2,y=580)
label = tk.Label(root, text="F12 - Nova Compra", bg="white").place(x=col2,y=600)

root.bind("<F1>", F1)
root.bind("<F2>", F2)
root.bind("<F3>", F3)
root.bind("<F4>", F4)
root.bind("<F5>", F5)
root.bind("<F12>", F12)

root.mainloop()