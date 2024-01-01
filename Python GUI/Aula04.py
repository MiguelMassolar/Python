import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Os pilares das interfaces gráficas")
janela["bg"] = "green"
janela.geometry("680x420+300+200")
Label(janela, text="Aula teórica!").pack()


janela.mainloop()