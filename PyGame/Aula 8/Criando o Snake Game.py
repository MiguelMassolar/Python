import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.mixer.init()
pygame.font.init()

pygame.mixer.music.set_volume(0.12)
musica_de_fundo = pygame.mixer.music.load("BoxCat Games - CPU Talk.mp3")
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.15)

largura = 640
altura = 480

'''Posição da cobra'''
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

'''Mantém a cobra se movendo'''
velocidade = 10
x_controle = velocidade
y_controle = 0

'''Reseta a posição da maçã aleatoriamente
ao iniciar o jogo'''
x_maca = randint(50, 600)
y_maca = randint(40, 430)

'''Altura e largura da Cobra e da Maçã!'''
A = 20
L = 20

fonte = pygame.font.SysFont('Arial', 40, True, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game Parte 1 e 2')
relogio = pygame.time.Clock()

'''Aqui deve ficar pois assim, não será resetado!'''
lista_cobra = []
comprimento_inicial = 5
morreu = False

'''Desenha o corpo da cobra da cobra'''
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], A, L))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(50, 600)
    y_maca = randint(40, 430)
    morreu = False

while True:

    relogio.tick(30)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Controles
        # Lembre que o cartesiano esta de ponta cabeça!
        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    '''A cobra não vai mais andar nas diagonais e não vai parar!'''
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    '''Cria os retângulos na tela'''
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, A, L))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, A, L))

    if cobra.colliderect(maca):
        x_maca = randint(50, 600)
        y_maca = randint(40, 430)
        comprimento_inicial = comprimento_inicial + 1 #Fará com que a cobra aumente ao comer!
        pontos = pontos + 1
        barulho_colisao.play()

    '''Armazena as posições atuais da cobra.'''
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    '''Armazena as posições totais da cobra'''
    lista_cobra.append(lista_cabeca)

    '''Criando o Game Over'''
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('Arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente.'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect() #Alinha o texto na tela!

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    '''Impede a cobra de sumir na tela Direita e Esquerda!'''
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura

    '''Impede da cobra de sumir na tela emcima e embaixo!'''
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    '''Chama a função que vai desenhar a cobra.'''
    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (420, 40))
    pygame.display.update()
