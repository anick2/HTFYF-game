import pygame
import const


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        self.image = pygame.Surface((width, height)).convert()
        self.image.fill((0, 255, 0))            #green
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)



