import sys
import pygame
from .state import *

sys.path.append('..')

from init import *
#import hero 
from sprites import * 

# класс для состояния "лес"
class Forest(State):          
    def __init__(self):
        State.__init__(self)
        self.on_create();
        
        self.set_background()

    def set_background(self):
        self.background = IMAGES['forest']
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height
        
        self.level = pygame.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = screen.get_rect(bottom=self.level_rect.bottom)
        
        self.level.blit(self.background, self.viewport, self.viewport)
        screen.blit(self.level, (0,0), self.viewport)
        
    def on_create(self):      
        pygame.display.flip()
        self.set_background()
        self.set_hero()
        self.set_blocks()
        self.set_enemies()
        self.set_checkpoints()

    def set_hero(self):
        '''self.hero = hero.Hero()
        self.hero.rect.x = self.viewport.x + 110
        self.hero.rect.bottom = c.HEIGHT_OF_GROUND'''
        pass

    def set_blocks(self):
        ground = Barrier(0, c.HEIGHT_OF_GROUND, 3000, 60)

    def set_enemies(self):
        pass

    def set_checkpoints(self):
        '''при столкновении героя с чекпоинтами появляются враги'''
        pass

    def on_update(self, keys):
        pygame.display.flip()
        self.update_everything(keys)
        self.blit_everything()


    def update_everything(self, keys):
       # self.hero.update(keys, self.powerup_group)
        self.check_cp()
        
    def blit_everything(self):
        pass

    def check_cp(self):
        ''' check check points'''
        pass
    
    
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True
