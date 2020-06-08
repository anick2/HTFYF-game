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
        ground = Barrier(0, c.HEIGHT_OF_GROUND, 3000, 40)

        block1 = Block(0, 560)
        block2 = Block(40, 560)
        block3 = Block(80, 560)
        block4 = Block(120, 560)
        block5 = Block(160, 560)
        block6 = Block(200, 560)
        block7 = Block(240, 560)
        block8 = Block(280, 560)
        block9 = Block(320, 560)
        block12 = Block(360, 560)
        block13 = Block(400, 560)
        block14 = Block(440, 560)
        block15 = Block(480, 560)
        block16 = Block(520, 560)
        block17 = Block(560, 560)
        block18 = Block(600, 560)
        block19 = Block(640, 560)
        block22 = Block(680, 560)
        block23 = Block(720, 560)
        block24 = Block(760, 560)
        block25 = Block(800, 560)
        block26 = Block(840, 560)
        block27 = Block(880, 560)
        block28 = Block(920, 560)
        block29 = Block(960, 560)

        self.blocks = pygame.sprite.Group(block1, block2, block3,
                                          block4, block5, block6,
                                          block7, block8, block9,
                                          block12, block13,
                                          block14, block15, block16,
                                          block17, block18, block19,
                                          block22, block23,
                                          block24, block25, block26,
                                          block27, block28, block29)
        

    def set_enemies(self):
        pass

    def set_checkpoints(self):
        '''при столкновении героя с чекпоинтами появляются враги'''
        pass

    def on_update(self, keys):
        self.update_everything(keys)
        self.blit_everything()
        self.update_viewport()


    def update_everything(self, keys):
        self.hero.update(keys, {})
        self.check_cp()
        self.sprite_positions()


    def sprite_positions(self):
        """Adjusts sprites by their x and y velocities and collisions"""
        self.hero_position()

        
    def hero_position(self):
        """Adjusts Mario's position based on his x, y velocities and
        potential collisions"""
        self.last_x_position = self.hero.rect.right
        self.hero.rect.x += round(self.hero.x_vel)
        self.x_collisions_hero()

        self.hero.rect.y += round(self.hero.y_vel)
        #self.y_collisions_hero()

        if self.hero.rect.x < (self.viewport.x + 5):
            self.hero.rect.x = (self.viewport.x + 5)


    def x_collisions_hero(self):
        bricks = pygame.sprite.spritecollideany(self.hero, self.blocks)
        
        if bricks:
            self.x_collisions_solve(bricks)


    def x_collisions_solve(self, collider):
        self.hero.x_vel = 0
        if self.hero.rect.x < collider.rect.x:
            self.hero.rect.right = collider.rect.left
        else:
            self.hero.rect.left = collider.rect.right

        
    def blit_everything(self):
        pygame.display.flip()
        self.level.blit(self.background, self.viewport, self.viewport)
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


    def update_viewport(self):
        third = self.viewport.x + self.viewport.w//3
        play_center = self.hero.rect.centerx
        play_right = self.hero.rect.right

        if self.hero.x_vel > 0 and play_center >= third:
            mult = 0.5 if play_right < self.viewport.centerx else 1
            new = self.viewport.x + mult * self.hero.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)
