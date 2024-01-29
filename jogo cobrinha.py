import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

velocidade = 5
l = 640
a = 480
r = pygame.time.Clock()
x = 0
y = 0
z =  random.randint(50, 600)
w = random.randint(50,400)
f = pygame.font.SysFont('arial',40, True,True)
p =  0
ai = l/2
li = 300
t = pygame.display.set_mode((l , a))

pygame.display.set_caption('jogo')
mf = pygame.mixer_music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

mb = pygame.mixer.Sound('smw_coin (1).wav')
while True:
    r.tick(60)
    t.fill((0, 0 ,0))
    m = f'pontos {p}'
    m2 = f'game over'
    tf = f.render(m, True, (250, 250,250))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                y = y+ 20
        if event.type == KEYDOWN:
            if event.key == K_w:
                y = y-20
        if event.type == KEYDOWN:
            if event.key == K_d:
                x= x+20
        if event.type == KEYDOWN:
            if event.key == K_a:
                x=x-20

    v = pygame.draw.rect(t, (150,0,150), (x,y, 50,50))
    az = pygame.draw.rect(t, (0, 250, 0), (z, w, 50, 50))
    inimigo = pygame.draw.rect(t ,(250,0,0),(ai,li,50,50))
    li = li + velocidade
    if li >= a:
        li = 0
    if az.colliderect(v):
         z = random.randint(0, 600)
         w = random.randint(0, 400)
         p = p+1
         mb.play(1)
    if v.colliderect(inimigo):
        pygame.quit()
        exit()




    t.blit(tf, (450, 40))


    pygame.display.update()
