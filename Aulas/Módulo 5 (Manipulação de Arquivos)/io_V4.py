
try:
    arquivo = open('D:/Users/Miguel/Documents/Estudos Python/Python/Aulas/Módulo 5 (Manipulação de Arquivos)/pessoas.csv')

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(registro.strip().split(',')))
        
finally:
    arquivo.close()
    
if arquivo.closed:
    print('Arquivo já foi fechado!')