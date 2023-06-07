import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

cor_branca = (255, 255, 255)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meus Sprites")


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe Sprite!
        self.sprites = []
        self.sprites.append(pygame.image.load('sprite_0.png'))
        self.sprites.append(pygame.image.load('sprite_1.png'))
        self.sprites.append(pygame.image.load('sprite_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 7, 32 * 7))  # Ajusta o tamanho da imagem.

        self.rect = self.image.get_rect()
        self.rect.topleft = 200, 200

    def update(self):
        self.atual = self.atual + 0.5  # Deixa a animação mais lenta
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]  # Converte os números para inteiro!
        self.image = pygame.transform.scale(self.image, (32 * 7, 32 * 7))


todas_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_sprites.add(personagem)

"""Adiciona o background para o jogo!"""
imagem_fundo = pygame.image.load('cidade_fundo_Persegan.jpg').convert()  # Melhora a perfomance do pygame!
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(35)
    tela.fill(cor_branca)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagem_fundo, (0, 0))
    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()
