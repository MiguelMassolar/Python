#!"C:\Program Files\Python311\python.exe"
import math
import sys

def circulo(raio):
    return math.pi * float(raio) ** 2

if __name__=='__main__':
    raio = sys.argv[0]
    area = circulo(raio)
    print('Área do circulo', area)