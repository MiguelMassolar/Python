import csv

with open('D:/Users/Miguel/Documents/Estudos Python/Python/Aulas/Módulo 5 (Manipulação de Arquivos)/pessoas.csv') as entrada:
    
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))