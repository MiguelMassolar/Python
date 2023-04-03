import pygame as pg
from pygame.locals import *
from sys import exit

pg.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Controlando Objetos')
relogio = pg.time.Clock()

while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        
        #Controles
        '''if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 20
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_UP:#Lembre que o cartesiano esta de ponta cabeça!
                y = y - 20
            if event.key == K_DOWN:
                y = y + 20'''
                
    if pg.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pg.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pg.key.get_pressed()[K_UP]:
        y = y - 5
    if pg.key.get_pressed()[K_DOWN]:
        y = y + 5
    
    pg.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    
    pg.display.update()