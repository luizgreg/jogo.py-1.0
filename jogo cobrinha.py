import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

l = 640
a = 480
r = pygame.time.Clock()
lista_cobra = []
comprimeto_maximo= 5
x = l/2
y = a/2


velocidade = 10
x_controle= velocidade
y_controle= 0


z =  random.randint(50, 600)
w = random.randint(50,400)

f = pygame.font.SysFont('arial',40, True,True)

p = 0

t = pygame.display.set_mode((l , a))
pygame.display.set_caption('jogo')
mf = pygame.mixer_music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

mb = pygame.mixer.Sound('smw_coin (1).wav')

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:

        pygame.draw.rect(t,(0,255,0), (xey[0], xey[1],20,20))

morreu = False


def r_j():
    global p, comprimeto_maximo, x, y, lista_cobra, lista_cabeca, z, w, morreu
    p = 0
    comprimeto_maximo = 5
    x = int(l / 2)
    y  = int(a / 2)
    lista_cobra = []
    lista_cabeca = []
    z = random.randint(40, 600)
    w = random.randint(50, 430)
    morreu = False


while True:
    r.tick(30)
    t.fill((250, 250 ,250))
    m = f'pontos {p}'
    tf = f.render(m, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle= velocidade
                    x_controle= 0


            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle= -velocidade
                    x_controle= 0


            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle= velocidade
                    y_controle= 0

            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle= -velocidade
                    y_controle= 0

    x = x+x_controle
    y = y+y_controle
    cobra = pygame.draw.rect(t, (0,255,0), (x,y, 20,20))
    maça = pygame.draw.rect(t, (250,0,0),(z,w,20,20))
    if maça.colliderect(cobra):
         z = random.randint(0, 600)
         w = random.randint(0, 400)
         p = p+1
         mb.play(1)
         comprimeto_maximo = comprimeto_maximo+1





    lista_cabeça = []
    lista_cabeça.append(x)
    lista_cabeça.append(y)
    lista_cobra.append(lista_cabeça)

    if len(lista_cobra) > comprimeto_maximo:
        del lista_cobra[0]


    aumenta_cobra(lista_cobra)

    t.blit(tf, (450, 40))
    if lista_cobra.count(lista_cabeça) > 1:
        f2 = pygame.font.SysFont('arial', 20, True, True)
        m2 = ('game over  precione r')
        tf2 = f2.render(m2, True, (250,0,0))

        morreu = True
        while morreu == True:
            t.fill((0, 0, 0))
            for event in pygame.event.get():
                t.fill((0,0,0))
                if event == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        r_j()
            t.blit(tf2,  (l//2,a//2))
            pygame.display.update()

    if x > l:
        x = 0
    if y > a:
        y = 0
    if x < 0:
        x = l
    if y < 0:
        y=a
    if len(lista_cobra) > comprimeto_maximo:
        del lista_cobra[0]





    pygame.display.update()
