import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

'''Reseta a posição do ret_azul aleatoriamente
ao iniciar o jogo'''
x_azul = randint(50, 600)
y_azul = randint(40, 430)
#Altura e largura dos retangulos
A = 40
L = 50

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Colisões')
relogio = pygame.time.Clock()

while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
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
                
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 5
    if pygame.key.get_pressed()[K_UP]:
        y = y - 5
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 5
        
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, A, L))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul, y_azul, A, L))
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(50, 600)
        y_azul = randint(40, 430)
    
    pygame.display.update()