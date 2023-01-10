import pygame, random
from pygame.locals import *

fps = pygame.time.Clock()

pygame.init()
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Aventura')

while True:
    fps.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    pygame.display.update()