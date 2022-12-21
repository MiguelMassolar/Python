from tkinter import *

class digaNome:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.titulo = Label(self.primeiroContainer, text="Por favor, digite o seu nome!")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()
        
        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        self.executar = Button(self.terceiroContainer)
        self.executar["text"] = "Executar"
        self.executar["font"] = ("Calibri", "8")
        self.executar["width"] = 12
        self.executar["command"] = self.digaNome
        self.executar.pack()
        
        self.mensagem = Label(self.quartoContainer, text=" ", font=self.fontePadrao)
        
    def digaNome(self):
        seuNome = self.nome.get()
        if seuNome == "Miguel":
            self.mensagem["text"] = "Que nome bonito! Prazer em te conhecer!"
        else:
            self.mensagem["text"] = "Prazer em te conhecer!"
        

root = Tk()
digaNome(root)
root.mainloop()
