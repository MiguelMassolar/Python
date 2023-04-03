import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.font.init()

largura = 640
altura = 480
x = int(largura / 2)
y = int(altura / 2)

'''Reseta a posição do ret_azul aleatoriamente
ao iniciar o jogo'''
x_azul = randint(50, 600)
y_azul = randint(40, 430)

x_amarelo = randint(30, 540)
y_amarelo = randint(15, 400)

x_violeta = randint(33, 520)
y_violeta = randint(10, 399)

# Altura e largura dos retangulos
A = 40
L = 50

fonte = pygame.font.SysFont('Arial', 40, True, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Inserindo textos e pontuações')
relogio = pygame.time.Clock()

while True:

    relogio.tick(120)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Controles
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

    # Cria os retângulos na tela
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, A, L))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, A, L))
    ret_amarelo = pygame.draw.rect(tela, (255, 255, 0), (x_amarelo, y_amarelo, A, L))
    ret_violeta = pygame.draw.rect(tela, (255,0,255), (x_violeta, y_violeta, A, L))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(50, 600)
        y_azul = randint(40, 430)
        pontos = pontos + 15

    if ret_vermelho.colliderect(ret_amarelo):
        x_amarelo = randint(30, 540)
        y_amarelo = randint(15, 400)
        pontos = pontos + 10

    if ret_vermelho.colliderect(ret_violeta):
        x_violeta = randint(33, 520)
        y_violeta = randint(10, 399)
        pontos = pontos + 100

    tela.blit(texto_formatado, (420, 40))
    pygame.display.update()