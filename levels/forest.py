import sys
import pygame
from .state import *

sys.path.append('..')

from init import *
import hero 
import enemies
import checkpoint
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
        self.set_spritegroups()

    def set_hero(self):
        self.hero = hero.Hero()
        self.hero.rect.x = self.viewport.x + 110
        self.hero.rect.bottom = 500
        pass

    def set_blocks(self):
        self.ground = Barrier(0, c.HEIGHT_OF_GROUND, 3000, 40)

        block1 = Block(100, 100)
        block2 = Block(140, 100)

        self.blocks = pygame.sprite.Group(block1, block2)
        

    def set_enemies(self):
        mushroom0 = enemies.Mushroom()
        mushroom1 = enemies.Mushroom()
        enemy_group1 = pygame.sprite.Group(mushroom0, mushroom1)
        self.enemy_group_list = [enemy_group1]

    def set_checkpoints(self):
        '''при столкновении героя с чекпоинтами появляются враги'''
        check1 = checkpoint.Checkpoint(110, "1")
        check2 = checkpoint.Checkpoint(550, '2')
        self.check_point_group = pygame.sprite.Group(check1, check2)

    def set_spritegroups(self):
        """Sprite groups created for convenience"""
        #self.sprites_about_to_die_group = pg.sprite.Group()
        #self.shell_group = pg.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        #self.ground_step_pipe_group = pg.sprite.Group(self.ground_group,
                                                      #self.pipe_group,
                                                      #self.step_group)

        self.hero_and_enemy_group = pygame.sprite.Group(self.hero,
                                                     self.enemy_group)

    def on_update(self, keys):
        self.update_everything(keys)
        self.blit_everything()


    def update_everything(self, keys):
        self.hero.update(keys, {})
        self.check_cp()
        self.enemy_group.update(keys)

        
    def blit_everything(self):
        pygame.display.flip()
        self.level.blit(self.background, self.viewport, self.viewport)
        self.level.blit(self.ground.image, (0,560))
        #self.level.blit(self.hero.image, (self.hero.pos_x,430))

        self.hero_and_enemy_group.draw(self.level)

        self.blocks.draw(self.level)
        screen.blit(self.level, (0,0), self.viewport)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));
        

    def check_cp(self):
        ''' check check points'''
        checkpoint = pygame.sprite.spritecollideany(self.hero,
                                                 self.check_point_group)
        if checkpoint:
            checkpoint.kill()
            for i in range(1,3):
                if checkpoint.name == str(i):
                    for index, enemy in enumerate(self.enemy_group_list[i -1]):
                        enemy.rect.x = self.viewport.right + (index * 60)
                    self.enemy_group.add(self.enemy_group_list[i-1])
            self.hero_and_enemy_group.add(self.enemy_group)

    '''def adjust_sprite_positions(self):
        """Регулирует спрайты по их скоростям x и y и столкновениям"""
        self.adjust_mario_position()
        self.adjust_enemy_position()'''
        
    
    
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True
