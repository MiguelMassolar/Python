#Importar o app e o Build(GUI)
#Criar o aplicativo
#Criar a função Build

#Inicialização do Aplicativo (Até o class).
from kivy.app import App
from kivy.lang import Builder
import requests
GUI = Builder.load_file("tela.kv")

class meuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar: R$ {self.pegarCotação('USD')}"
        self.root.ids["moeda2"].text = f"EURO: R$ {self.pegarCotação('EUR')}"
        self.root.ids["moeda3"].text = f"Argentina: R$ {self.pegarCotação('ARS')}"
        self.root.ids["moeda4"].text = f"Japão: R$ {self.pegarCotação('JPY')}"
        
    def pegarCotação(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisição = requests.get(link)
        dic_requisição = requisição.json()
        cotação = dic_requisição[f"{moeda}BRL"]["bid"]
        return cotação

meuAplicativo().run()