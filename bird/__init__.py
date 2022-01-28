
import pygame


class Bird:
    def __init__(self, local, pos_x, pos_y, scale_x, scale_y):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        #Escalonamento
        self.scale_y = scale_y
        self.scale_x = scale_x
        self.local = local
        self.sprite.image = pygame.image.load(local)
        self.sprite.image = pygame.transform.scale(self.sprite.image, (scale_x, scale_y))

        #Rect - Quadrado da image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = pos_x
        self.sprite.rect[1] = pos_y

        self.birds = ["sprites/flappybird-down-red.png",
                      "sprites/flappybird-mid-red.png",
                      "sprites/flappybird-up-red.png"]

        self.frame = 0

    def Upade_anim(self):
        self.frame = (self.frame + 1) % 3

        self.sprite.image = pygame.image.load(self.birds[self.frame])
        self.sprite.image = pygame.transform.scale(self.sprite.image, (self.scale_x, self.scale_y))
