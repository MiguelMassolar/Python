class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('Au Au!')
    def correr(self):
        print(f'{self.nome} está correndo!')

cachorro_1 = Cachorros('Toby', 'Marrom', 5, 'Grande')
print(cachorro_1.nome)
print(cachorro_1.cor_de_pelo)
print(cachorro_1.idade)
print(cachorro_1.tamanho)
cachorro_1.latir()
cachorro_1.correr()

cachorro_2 = Cachorros('Max', 'Preto', 3, 'Pequeno')
print(cachorro_2.nome)
print(cachorro_2.cor_de_pelo)
print(cachorro_2.idade)
print(cachorro_2.tamanho)
cachorro_2.latir()
cachorro_2.correr()