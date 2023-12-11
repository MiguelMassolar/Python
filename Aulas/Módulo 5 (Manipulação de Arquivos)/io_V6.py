
with open('D:/Users/Miguel/Documents/Estudos Python/Python/Aulas/Módulo 5 (Manipulação de Arquivos)/pessoas.csv') as arquivo:
    
    with open('D:/Users/Miguel/Documents/Estudos Python/Python/Aulas/Módulo 5 (Manipulação de Arquivos)/pessoas.txt', 'w') as saida:
        
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
    
if arquivo.close:
    print('O qrquivo já foi fechado!')
    
if saida.close:
    print('O arquivo de saída já foi fechado!')