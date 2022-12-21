from tkinter import *

janela = Tk()

lb = Label(janela, text="Fala galera!")
lb.place(x=100, y=100)

janela.geometry("300x300+200+200") #primeiro width x Height, + Left + Top

janela.mainloop()