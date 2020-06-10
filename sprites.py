import pygame
import const
from init import *


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        self.image = pygame.Surface((width, height)).convert()
        self.image.fill((0, 255, 0))            #green
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 600 - y


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, s):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        
        img = pygame.transform.scale(IMAGES['block_' + s], c.BLOCK_SIZE)     
        self.image = pygame.Surface(c.BLOCK_SIZE).convert()
        self.image.set_colorkey((0,0,0))
        self.image.blit(img, (0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



