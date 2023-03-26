import pygame as pg
from pygame.locals import *
from sys import exit

pg.init()

largura = 640
altura = 480
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Jooj')

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    pg.display.update()