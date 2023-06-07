import pygame as pg
from pygame.locals import *
from sys import exit

pg.init()
pg.font.init()

largura = 600
altura = 600

altura_player = 20
largura_player = 20

altura_chao = -200
largura_chao = 498

fonte = pg.font.SysFont('Arial', 40, True, True)
tela = pg.display.set_mode((largura, altura))
relogio = pg.time.Clock()
pg.display.set_caption('Jooj')

while True:

    relogio.tick(30)
    tela.fill((0,0,0))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

    player = pg.draw.rect(tela, (255,255,255), )
    chao = pg.draw.rect(tela, (0,255,0))
    pg.display.update()