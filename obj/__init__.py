
import pygame


class Obj:
    def __init__(self, local, pos_x, pos_y, scale_x, scale_y):
        """
        :param local: Local onde se encontra a sprite
        :param pos_x: posição x da srite na matriz
        :param pos_y: posição y da srite na matriz
        :param scale_x: escalonamento da pos_x
        :param scale_y: escalonamento da pos_y
        """
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        #Escalonamento
        self.sprite.image = pygame.image.load(local)
        self.sprite.image = pygame.transform.scale(self.sprite.image, (scale_x, scale_y))

        #Rect - Quadrado da image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = pos_x
        self.sprite.rect[1] = pos_y

