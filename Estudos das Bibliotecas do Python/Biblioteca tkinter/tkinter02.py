import tkinter as tk

janela = tk.Tk()
janela.title("Janela Principal")
janela["bg"] = "green" #background entre colchetes também funciona!
janela.geometry("800x300+100+100")#LxA+E+T ex: 300x300+100+100

janela.mainloop()