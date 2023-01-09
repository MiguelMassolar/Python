#Jogo ensinado por (https://www.youtube.com/@ProgramadorSagaz) Programador Sagaz no YouTube!!!
import pygame, random
from pygame.locals import *

#Isto vai alinhar a maçã e a cobra
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 * 10, y//10 * 10)

#Crindao a colizão do Jogo
def colizão(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

#Controle para o jogo
UP = 0 
RIGHT = 1
DOWN = 2
LEFT = 3

fps = pygame.time.Clock() #controla a velocidade do jogo!

#Inicializador e Estabelece o display(tela) do jogo
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

#Skin da Cobra
cobra = [(200,200), (210,200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255))

#Skin da maçã e posição
maçã_pos = on_grid_random()
maçã = pygame.Surface((10,10))
maçã.fill((255,0,0))

direção = LEFT

while True:
    fps.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        #Controles do Jogo!
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direção = UP
            if event.key == K_DOWN:
                direção = DOWN
            if event.key == K_LEFT:
                direção = LEFT
            if event.key == K_RIGHT:
                direção = RIGHT
    
    #Inserindo a Colisão no Jogo
    if colizão(cobra[0], maçã_pos):
        maçã_pos = on_grid_random()
        cobra.append((0,0))
    
    for i in range(len(cobra) -1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
    
    #Estabelecendo as direções
    if direção == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] -10)
    if direção == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] +10)
    if direção == RIGHT:
        cobra[0] = (cobra[0][0] +10, cobra[0][1])
    if direção == LEFT:
        cobra[0] = (cobra[0][0] -10, cobra[0][1])
        
    #Definindo as cores da Cobra/Maçã    
    screen.fill((0,0,0))
    screen.blit(maçã, maçã_pos)
    for pos in cobra:
        screen.blit(cobra_skin,pos)
    
    #Atualiza a tela do Jogo        
    pygame.display.update()