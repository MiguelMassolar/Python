
with open('D:/Users/Miguel/Documents/Estudos Python/Python/Aulas/Módulo 5 (Manipulação de Arquivos)/pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
    
if arquivo.close:
    print('O qrquivo já foi fechado!')