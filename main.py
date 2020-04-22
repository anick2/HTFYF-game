import pygame
import sys
import os

clock = pygame.time.Clock()
pygame.init()

worldx = 800
worldy = 336

world       = pygame.display.set_mode([worldx,worldy])
backdrop    = pygame.image.load(os.path.join('nat.png')).convert()
backdropbox = world.get_rect()

'''
Objects
'''

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load('hero.png').convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey((255,255,255)) # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()

'''
Setup
'''

player = Player()   # spawn player
player.rect.x = 30   # go to x
player.rect.y = 30   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

main = True

'''
Main loop
'''
fps   = 40  # frame rate
ani   = 4   # animation cycles

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    pygame.display.flip()
    world.blit(backdrop, backdropbox)
    player_list.draw(world) # draw player
    
clock.tick(fps)
