import pygame
import const as c
import init


class Barrier(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        self.image = pygame.Surface((width, height)).convert()
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 600 - y


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, s):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        img = pygame.transform.scale(init.IMAGES['block_' + s], c.BLOCK_SIZE)
        self.image = pygame.Surface(c.BLOCK_SIZE).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        self.frame_index = 0
        img = pygame.transform.scale(init.IMAGES['coin'
                                     + str(self.frame_index)], (25, 25))
        self.image = pygame.Surface((25, 25)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.frame_index += 1
        self.frame_index = self.frame_index % 6
        img = pygame.transform.scale(init.IMAGES['coin'
                                     + str(self.frame_index)], (25, 25))
        self.image = pygame.Surface((25, 25)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(img, (0, 0))


class Info_coin(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = None
        self.number = c.COINS
        self.color = pygame.Color('yellow')
        self.font = pygame.font.SysFont('meslolgmboldforpowerlinettf', 30)
        fon = self.font.render(str(self.number) + ' x', True, self.color)
        fon_rect = fon.get_rect()
        self.w = fon_rect.height + fon_rect.width + 10
        self.frame_index = 0
        self.image = pygame.Surface((fon_rect.height + fon_rect.width
                                     + 10, fon_rect.height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 20

    def update(self):
        self.frame_index += 1
        self.frame_index = self.frame_index % 6
        fon = self.font.render(str(self.number) + ' x', True, self.color)
        fon_rect = fon.get_rect()
        self.w = fon_rect.height + fon_rect.width + 10
        t1 = fon_rect.height - 5
        t2 = fon_rect.height - 5
        img = pygame.transform.scale(init.IMAGES['coin'
                                     + str(self.frame_index)], (t1, t2))
        t1 = fon_rect.height + fon_rect.width + 10
        t2 = fon_rect.height
        self.image = pygame.Surface((t1, t2)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(img, (fon_rect.width + 4, 0))
        self.image.blit(fon, (0, 0))
        c.COINS = self.number


class Info_hearts(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.number = 3
        self.image = pygame.Surface((200, 70)).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        img = pygame.transform.scale(init.IMAGES['hearts'
                                     + str(self.number)], (200, 70))
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(img, (0, 0))


class Heal(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 30)).convert()
        self.rect = self.image.get_rect()
        img = pygame.transform.scale(init.IMAGES['bottle'], (20, 30))
        img.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(img, (0, 0))
        self.rect.x = x
        self.rect.y = y
