#!"C:\Program Files\Python311\python.exe"
from math import pi

def circulo(Raio):
    return pi * float(Raio) ** 2

if __name__ == '__main__':
    Raio = input('Informe o raio: ')
    area = circulo(Raio)
    print('Área do círculo', area)