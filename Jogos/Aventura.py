import pygame as py
from sys import exit

py.init()
screen = py.display.set_mode((800, 400))
py.display.set_caption('Aventura')

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    #Aqui ficará todos os elementos
    py.display.update()