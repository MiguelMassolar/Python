#!"C:\Program Files\Python311\python.exe"
import math

def circulo(Raio):
    print('Área do círclo:', math.pi * float(Raio) ** 2)

if __name__ == '__main__':
    Raio = input('Informe o raio: ')
    circulo(Raio)