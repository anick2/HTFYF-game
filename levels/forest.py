import sys
import pygame
from .state import *

sys.path.append('..')

from init import *
import hero 
from sprites import *
from sounds import *

# класс для состояния "лес"
class Forest(State):          
    def __init__(self):
        State.__init__(self)

    def set_background(self):
        self.background = IMAGES['forest']
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height
        
        self.level = pygame.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = screen.get_rect(bottom=self.level_rect.bottom)
        
        self.level.blit(self.background, (0, 0))
        screen.blit(self.level, (0,0), self.viewport)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));
        
        
    def on_create(self):      
        self.sound_player = Sound("FOREST")
        self.set_background()
        self.set_hero()
        self.set_blocks()
        self.set_enemies()
        self.set_checkpoints()

    def set_hero(self):
        self.hero = hero.Hero()
        self.hero.rect.x = self.viewport.x + 110
        self.hero.rect.bottom = 560
        self.pers = pygame.sprite.Group(self.hero)
        pass

    def set_blocks(self):
        self.ground = Barrier(0, c.HEIGHT_OF_GROUND, 3000, 40)

        block1 = Block(100, 100)
        block2 = Block(140, 100)

        self.blocks = pygame.sprite.Group(block1, block2, block3)
        

    def set_enemies(self):
        pass

    def set_checkpoints(self):
        '''при столкновении героя с чекпоинтами появляются враги'''
        pass

    def on_update(self, keys):
        self.update_everything(keys)
        self.blit_everything()


    def update_everything(self, keys):
        self.hero.update(keys, {})
        self.check_cp()
        self.adjust_sprite_positions()


    def adjust_sprite_positions(self):
        """Adjusts sprites by their x and y velocities and collisions"""
        self.adjust_mario_position()

        
    def adjust_mario_position(self):
        """Adjusts Mario's position based on his x, y velocities and
        potential collisions"""
        self.last_x_position = self.hero.rect.right
        self.hero.rect.x += round(self.hero.x_vel)
        #self.check_hero_x_collisions()

        self.hero.rect.y += round(self.hero.y_vel)
        #self.check_hero_y_collisions()

        if self.hero.rect.x < (self.viewport.x + 5):
            self.hero.rect.x = (self.viewport.x + 5)   

        
    def blit_everything(self):
        pygame.display.flip()
        self.level.blit(self.background, self.viewport, self.viewport)
        self.level.blit(self.ground.image, (0,560))
        #self.level.blit(self.hero.image, (self.hero.pos_x,430))
        self.blocks.draw(self.level)
        self.pers.draw(self.level)
        screen.blit(self.level, (0,0), self.viewport)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));
        pass

    def check_cp(self):
        ''' check check points'''
        pass
    
    
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True
