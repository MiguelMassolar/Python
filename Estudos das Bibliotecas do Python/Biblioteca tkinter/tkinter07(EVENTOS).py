from functools import partial
from tkinter import *

def btn_click(botao):
    print(botao["text"])

janela = Tk()

#não se usa parêntesis no command!!
bt1 = Button(janela, width=20, text="Botão 1")
bt1["command"] = partial(btn_click, bt1)
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text="Botão 2")
bt2["command"] = partial(btn_click, bt2)
bt2.place(x=100, y=130)

janela.geometry("300x300+200+200")
janela.mainloop()