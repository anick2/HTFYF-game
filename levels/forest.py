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

        
        block0 = Block(150, 500)
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

        block31 = Block(1000, 560)
        block32 = Block(1040, 560)
        block33 = Block(1080, 560)
        block34 = Block(1120, 560)
        block35 = Block(1160, 560)
        block36 = Block(1200, 560)
        block37 = Block(1240, 560)
        block38 = Block(1280, 560)
        block39 = Block(1320, 560)
        block42 = Block(1360, 560)
        block43 = Block(1400, 560)
        block44 = Block(1440, 560)
        block45 = Block(1480, 560)
        block46 = Block(1520, 560)
        block47 = Block(1560, 560)
        block48 = Block(1600, 560)
        block49 = Block(1640, 560)
        block52 = Block(1680, 560)
        block53 = Block(1720, 560)
        block54 = Block(1760, 560)
        block55 = Block(1800, 560)
        block56 = Block(1840, 560)
        block57 = Block(1880, 560)
        block58 = Block(1920, 560)
        block59 = Block(1960, 560)

        block61 = Block(2000, 560)
        block62 = Block(2040, 560)
        block63 = Block(2080, 560)
        block64 = Block(2120, 560)
        block65 = Block(2160, 560)
        block66 = Block(2200, 560)
        block67 = Block(2240, 560)
        block68 = Block(2280, 560)
        block69 = Block(2320, 560)
        block72 = Block(2360, 560)
        block73 = Block(2400, 560)
        block74 = Block(2440, 560)
        block75 = Block(2480, 560)
        block76 = Block(2520, 560)
        block77 = Block(2560, 560)
        block78 = Block(2600, 560)
        block79 = Block(2640, 560)
        block82 = Block(2680, 560)
        block83 = Block(2720, 560)
        block84 = Block(2760, 560)
        block85 = Block(2800, 560)
        block86 = Block(2840, 560)
        block87 = Block(2880, 560)
        block88 = Block(2920, 560)
        block89 = Block(2960, 560)

        block91 = Block(3000, 560)
        block92 = Block(3040, 560)
        block93 = Block(3080, 560)
        block94 = Block(3120, 560)
        block95 = Block(3160, 560)
        block96 = Block(3200, 560)
        block97 = Block(3240, 560)
        block98 = Block(3280, 560)
        block99 = Block(3320, 560)
        block102 = Block(3360, 560)
        block103 = Block(3400, 560)
        block104 = Block(3440, 560)
        block105 = Block(3480, 560)
        block106 = Block(3520, 560)
        block107 = Block(3560, 560)
        block108 = Block(3600, 560)
        block109 = Block(3640, 560)
        block112 = Block(3680, 560)
        block113 = Block(3720, 560)
        block114 = Block(3760, 560)
        block115 = Block(3800, 560)
        block116 = Block(3840, 560)
        block117 = Block(3880, 560)
        block118 = Block(3920, 560)
        block119 = Block(3960, 560)

        block121 = Block(4000, 560)
        block122 = Block(4040, 560)
        block123 = Block(4080, 560)
        block124 = Block(4120, 560)
        block125 = Block(4160, 560)
        block126 = Block(4200, 560)
        block127 = Block(4240, 560)
        block128 = Block(4280, 560)
        block129 = Block(4320, 560)
        block132 = Block(4360, 560)
        block133 = Block(4400, 560)
        block134 = Block(4440, 560)
        block135 = Block(4480, 560)
        block136 = Block(4520, 560)
        block137 = Block(4560, 560)
        block138 = Block(4600, 560)
        block139 = Block(4640, 560)
        block142 = Block(4680, 560)
        block143 = Block(4720, 560)
        block144 = Block(4760, 560)
        block145 = Block(4800, 560)
        block146 = Block(4840, 560)
        block147 = Block(4880, 560)
        block148 = Block(4920, 560)
        block149 = Block(4960, 560)

        block201 = Block(240, 520)
        block202 = Block(280, 520)
        block203 = Block(320, 520)
        block204 = Block(320, 480)
    
        
        self.blocks = pygame.sprite.Group(block1, block2, block3,
                                          block4, block5, block6,
                                          block7, block8, block9,
                                          block12, block13,
                                          block14, block15, block16,
                                          block17, block18, block19,
                                          block22, block23,
                                          block24, block25, block26,
                                          block27, block28, block29,
                                          block31, block32, block33,
                                          block34, block35, block36,
                                          block37, block38, block39,
                                          block42, block43,
                                          block44, block45, block46,
                                          block47, block48, block49,
                                          block52, block53,
                                          block54, block55, block56,
                                          block57, block58, block59,
                                          block61, block62, block63,
                                          block64, block65, block66,
                                          block67, block68, block69,
                                          block72, block73,
                                          block74, block75, block76,
                                          block77, block78, block79,
                                          block82, block83,
                                          block84, block85, block86,
                                          block87, block88, block89,
                                          block91, block92, block93,
                                          block94, block95, block96,
                                          block97, block98, block99,
                                          block102, block103,
                                          block104, block105, block106,
                                          block107, block108, block109,
                                          block112, block113,
                                          block114, block115, block116,
                                          block117, block118, block119,
                                          block121, block122, block123,
                                          block124, block125, block126,
                                          block127, block128, block129,
                                          block132, block133,
                                          block134, block135, block136,
                                          block137, block138, block139,
                                          block142, block143,
                                          block144, block145, block146,
                                          block147, block148, block149,

                                          block201, block202, block203, block204)
        

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
        self.y_collisions_hero()

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


    def y_collisions_hero(self):
        bricks = pygame.sprite.spritecollideany(self.hero, self.blocks)
        
        if bricks:
            self.hero.rect.bottom = bricks.rect.top
            self.hero.state = "WALK"
            self.hero.y_vel = 0



        
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
