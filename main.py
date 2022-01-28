
import pygame
from obj import Obj
from random import randint
from bird import Bird

pygame.init()
#Dimensões da matriz
largura = 360
altura = 640

#Velocidade de movimento das sprites
vel_anim = 4
vel = 4

#Gravidade
grvity = 1

jogando = True

window = pygame.display.set_mode((largura, altura))
window_tilte = pygame.display.set_caption('FlappyBird')

#Background
bg = Obj('sprites/flappybird-city-day.png', 0, 0, largura, altura)

#Bird
bird = Bird("sprites/flappybird-down-red.png", largura/4, altura/2, int(largura/6), int(altura/10))

pipe_y = randint(-180, 0)

#Pipe
pipe = Obj("sprites/block-green.png", largura, pipe_y, int(largura/5), int(altura/2.5))

coin = Obj('sprites/gold.png', pipe.sprite.rect[0] + 14, pipe_y + 325, int(largura/8), int(altura/13))

pipe2 = Obj("sprites/block-green.png", largura, pipe_y + 450, int(largura/5), int(altura/2.5))

#Ground
ground = Obj("sprites/flappy-bird-base.png", 0, int(altura - altura/5), largura, int(altura/5))
ground2 = Obj("sprites/flappy-bird-base.png", largura, int(altura - altura/5), largura, int(altura/5))


score = 0


def Draw():
    pygame.font.init()

    font_defaut = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font_defaut, 38, True)
    font_text = "{}".format(str(score))
    font_render = font_size.render(font_text, True, (255, 255, 255))

    window.blit(bg.sprite.image, bg.sprite.rect)
    window.blit(bird.sprite.image, bird.sprite.rect)
    window.blit(pipe.sprite.image, pipe.sprite.rect)
    window.blit(coin.sprite.image, coin.sprite.rect)
    window.blit(pygame.transform.flip(pipe2.sprite.image, False, True), pipe2.sprite.rect)
    window.blit(font_render, (int(largura/2), int(altura/15)))
    window.blit(ground.sprite.image, ground.sprite.rect)
    window.blit(ground2.sprite.image, ground2.sprite.rect)

    if jogando:
        # Ground Anim
        ground.sprite.rect[0] -= vel_anim
        ground2.sprite.rect[0] -= vel_anim
        if ground.sprite.rect[0] == -largura:
            ground.sprite.rect[0] = 0
        if ground2.sprite.rect[0] == 0:
            ground2.sprite.rect[0] = largura

        # Coin anim
        coin.sprite.rect[0] -= vel_anim

        # Pipe anim
        pipe.sprite.rect[0] -= vel_anim
        pipe2.sprite.rect[0] -= vel_anim
        if pipe.sprite.rect[0] == -100:
            pipe.sprite.rect[0] = largura
            pipe2.sprite.rect[0] = largura
            coin.sprite.rect[0] = pipe.sprite.rect[0] + 14
            pipe.sprite.rect[1] = randint(-180, 0)
            pipe2.sprite.rect[1] = pipe.sprite.rect[1] + 450
            coin.sprite.rect[1] = pipe.sprite.rect[1] + 325

        # Bird anim
        bird.sprite.rect[1] += vel
        # bird.rect[0] += vel
        if bird.sprite.rect[1] >= ground.sprite.rect[1] - bird.sprite.rect[3]:
            bird.sprite.rect[1] = ground.sprite.rect[1] - bird.sprite.rect[3]


def Colission():
    global score, jogando

    colisson_pipe = pygame.sprite.spritecollide(bird.sprite, pipe.group, False)
    colisson_pipe2 = pygame.sprite.spritecollide(bird.sprite, pipe2.group, False)
    colisson_coin = pygame.sprite.spritecollide(bird.sprite, coin.group, False)

    if colisson_pipe or colisson_pipe2:
        jogando = False
    elif colisson_coin:
        score += 1
        coin.sprite.rect[1] = -50


def Game_Over():
    pass


#FPS
clock = pygame.time.Clock()

loop = True
while loop:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if jogando:
                if bird.sprite.rect[1] > 10:
                    vel += 12 * -1

    #Movimento de queda
    if vel < 10:
        vel += grvity
    elif vel > 10:
        vel = 1

    #Limitação superior do bird
    if bird.sprite.rect[1] < 0:
        bird.sprite.rect[1] = 0
        vel = 4

    if jogando:
        Draw()
        Colission()
        bird.Upade_anim()
        
    pygame.display.update()
