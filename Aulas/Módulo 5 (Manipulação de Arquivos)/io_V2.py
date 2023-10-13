arquivo = open('D:/Users/Miguel/Documents/Estudos Python/Python/Aulas/Módulo 5 (Manipulação de Arquivos)/pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {} Idade: {}'.format(*registro.split(',')))