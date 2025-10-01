import tkinter as tk

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

#linha 1
Subotao = tk.Entry(root, textvariable=SubValor, width=12, font=("Arial", 20, "")).place(x=col1,y=(40 + (4.28 * 0)))
desbotao = tk.Entry(root, textvariable=DesValor, width=12, font=("Arial", 20, "")).place(x=col2,y=(40 + (4.28 * 0)))

label = tk.Label(root, text="Sub-Total").place(x=col1,y=(40 + (4.28 * 0)) - 25)
label = tk.Label(root, text="Desconto").place(x=col2,y=(40 + (4.28 * 0)) - 25)

#linha 2
tobotao = tk.Entry(root, textvariable=TotalValor, width=24, font=("Arial", 25, "")).place(x=col1,y=(40 * (4.28 * 1)) + 10)
label = tk.Label(root, text="Total").place(x=col1,y=(40 * (4.28 * 1))- 15)

#linha 3
Subotao = tk.Entry(root, textvariable=ResValor, width=12, font=("Arial", 20, "")).place(x=col1,y=(40 * (4.28 * 2)))
desbotao = tk.Entry(root, textvariable=TroValor, width=12, font=("Arial", 20, "")).place(x=col2,y=(40 * (4.28 * 2)))

label = tk.Label(root, text="Valor Recebido").place(x=col1,y=(40 * (4.28 * 2)) - 25)
label = tk.Label(root, text="Troco").place(x=col2,y=(40 * (4.28 * 2))- 25)

#o famoso listbox
listbox = tk.Listbox(root, height=20, width=50).place(x=10,y=40)
label = tk.Label(root, text="Lista de Produtos").place(x=140,y=10)


root.mainloop()