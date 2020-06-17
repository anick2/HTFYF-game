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

class Park(State):
    # класс для состояния "парк"
    def __init__(self):
        State.__init__(self)

    def set_background(self):
        self.background = IMAGES['park']
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
        # self.sound_player = Sound("FOREST")
        self.set_background()
        self.set_hero()
        self.set_blocks()
        self.set_enemies()
        self.set_coins()
        self.set_checkpoints()
        self.set_spritegroups()

    def set_hero(self):
        self.hero = hero.Hero()
        self.hero.rect.x = self.viewport.x + 110
        self.hero.rect.bottom = 560
        self.pers = pygame.sprite.Group(self.hero)
        self.info_coin = Info()
        self.info = pygame.sprite.Group(self.info_coin)

    def set_coins(self):
        coin1 = Coin(100, 450)
        coin2 = Coin(100, 100)
        self.coins = pygame.sprite.Group(coin1, coin2)


    def set_blocks(self):
        self.ground = Barrier(0, c.HEIGHT_OF_GROUND, 3000, 40)

        block0 = Block(1080, 40, 'park')
        block1 = Block(2640, 40, 'park')
        block2 = Block(1080, 80, 'park')
        block3 = Block(2640, 80, 'park')
        block4 = Block(3400, 80, 'park')
        block5 = Block(1080, 120, 'park')
        block6 = Block(2240, 120, 'park')
        block7 = Block(2320, 120, 'park')
        block8 = Block(2400, 120, 'park')
        block9 = Block(2480, 120, 'park')
        block10 = Block(2640, 120, 'park')
        block11 = Block(3400, 120, 'park')
        block12 = Block(4200, 120, 'park')
        block13 = Block(1080, 160, 'park')
        block14 = Block(1760, 160, 'park')
        block15 = Block(1800, 160, 'park')
        block16 = Block(1840, 160, 'park')
        block17 = Block(1880, 160, 'park')
        block18 = Block(1920, 160, 'park')
        block19 = Block(1960, 160, 'park')
        block20 = Block(2640, 160, 'park')
        block21 = Block(2680, 160, 'park')
        block22 = Block(2720, 160, 'park')
        block23 = Block(2840, 160, 'park')
        block24 = Block(2880, 160, 'park')
        block25 = Block(2920, 160, 'park')
        block26 = Block(2960, 160, 'park')
        block27 = Block(3000, 160, 'park')
        block28 = Block(3040, 160, 'park')
        block29 = Block(3080, 160, 'park')
        block30 = Block(3120, 160, 'park')
        block31 = Block(3160, 160, 'park')
        block32 = Block(3200, 160, 'park')
        block33 = Block(3240, 160, 'park')
        block34 = Block(3400, 160, 'park')
        block35 = Block(4280, 160, 'park')
        block36 = Block(120, 200, 'park')
        block37 = Block(240, 200, 'park')
        block38 = Block(360, 200, 'park')
        block39 = Block(400, 200, 'park')
        block40 = Block(440, 200, 'park')
        block41 = Block(560, 200, 'park')
        block42 = Block(1080, 200, 'park')
        block43 = Block(1680, 200, 'park')
        block44 = Block(2040, 200, 'park')
        block45 = Block(2080, 200, 'park')
        block46 = Block(2200, 200, 'park')
        block47 = Block(2280, 200, 'park')
        block48 = Block(2360, 200, 'park')
        block49 = Block(2440, 200, 'park')
        block50 = Block(2520, 200, 'park')
        block51 = Block(3000, 200, 'park')
        block52 = Block(3400, 200, 'park')
        block53 = Block(4160, 200, 'park')
        block54 = Block(1000, 240, 'park')
        block55 = Block(1160, 240, 'park')
        block56 = Block(1960, 240, 'park')
        block57 = Block(2200, 240, 'park')
        block58 = Block(2360, 240, 'park')
        block59 = Block(2520, 240, 'park')
        block60 = Block(2760, 240, 'park')
        block61 = Block(3000, 240, 'park')
        block62 = Block(3400, 240, 'park')
        block63 = Block(3880, 240, 'park')
        block64 = Block(3920, 240, 'park')
        block65 = Block(3960, 240, 'park')
        block66 = Block(4000, 240, 'park')
        block67 = Block(4040, 240, 'park')
        block68 = Block(4080, 240, 'park')
        block69 = Block(4160, 240, 'park')
        block70 = Block(4320, 240, 'park')
        block71 = Block(520, 280, 'park')
        block72 = Block(680, 280, 'park')
        block73 = Block(1600, 280, 'park')
        block74 = Block(1960, 280, 'park')
        block75 = Block(2200, 280, 'park')
        block76 = Block(2360, 280, 'park')
        block77 = Block(2520, 280, 'park')
        block78 = Block(3000, 280, 'park')
        block79 = Block(3400, 280, 'park')
        block80 = Block(4160, 280, 'park')
        block81 = Block(4200, 280, 'park')
        block82 = Block(960, 320, 'park')
        block83 = Block(1040, 320, 'park')
        block84 = Block(1080, 320, 'park')
        block85 = Block(1120, 320, 'park')
        block86 = Block(1200, 320, 'park')
        block87 = Block(2200, 320, 'park')
        block88 = Block(2360, 320, 'park')
        block89 = Block(2520, 320, 'park')
        block90 = Block(2840, 320, 'park')
        block91 = Block(3000, 320, 'park')
        block92 = Block(3400, 320, 'park')
        block93 = Block(3800, 320, 'park')
        block94 = Block(4160, 320, 'park')
        block95 = Block(4200, 320, 'park')
        block96 = Block(4320, 320, 'park')
        block97 = Block(440, 360, 'park')
        block98 = Block(480, 360, 'park')
        block99 = Block(880, 360, 'park')
        block100 = Block(1560, 360, 'park')
        block101 = Block(1680, 360, 'park')
        block102 = Block(1720, 360, 'park')
        block103 = Block(1760, 360, 'park')
        block104 = Block(1800, 360, 'park')
        block105 = Block(1840, 360, 'park')
        block106 = Block(1880, 360, 'park')
        block107 = Block(1920, 360, 'park')
        block108 = Block(1960, 360, 'park')
        block109 = Block(2200, 360, 'park')
        block110 = Block(2360, 360, 'park')
        block111 = Block(2520, 360, 'park')
        block112 = Block(3000, 360, 'park')
        block113 = Block(3160, 360, 'park')
        block114 = Block(3200, 360, 'park')
        block115 = Block(3240, 360, 'park')
        block116 = Block(3280, 360, 'park')
        block117 = Block(3320, 360, 'park')
        block118 = Block(3360, 360, 'park')
        block119 = Block(3400, 360, 'park')
        block120 = Block(4160, 360, 'park')
        block121 = Block(4200, 360, 'park')
        block122 = Block(4240, 360, 'park')
        block123 = Block(800, 400, 'park')
        block124 = Block(2200, 400, 'park')
        block125 = Block(2360, 400, 'park')
        block126 = Block(2520, 400, 'park')
        block127 = Block(2760, 400, 'park')
        block128 = Block(3000, 400, 'park')
        block129 = Block(3720, 400, 'park')
        block130 = Block(3880, 400, 'park')
        block131 = Block(3920, 400, 'park')
        block132 = Block(3960, 400, 'park')
        block133 = Block(4000, 400, 'park')
        block134 = Block(4120, 400, 'park')
        block135 = Block(4160, 400, 'park')
        block136 = Block(4200, 400, 'park')
        block137 = Block(4240, 400, 'park')
        block138 = Block(4280, 400, 'park')
        block139 = Block(4320, 400, 'park')
        block140 = Block(360, 440, 'park')
        block141 = Block(400, 440, 'park')
        block142 = Block(1080, 440, 'park')
        block143 = Block(1520, 440, 'park')
        block144 = Block(1720, 440, 'park')
        block145 = Block(2200, 440, 'park')
        block146 = Block(2360, 440, 'park')
        block147 = Block(2520, 440, 'park')
        block148 = Block(3000, 440, 'park')
        block149 = Block(4040, 440, 'park')
        block150 = Block(360, 480, 'park')
        block151 = Block(600, 480, 'park')
        block152 = Block(680, 480, 'park')
        block153 = Block(760, 480, 'park')
        block154 = Block(1040, 480, 'park')
        block155 = Block(1120, 480, 'park')
        block156 = Block(1720, 480, 'park')
        block157 = Block(2280, 480, 'park')
        block158 = Block(2440, 480, 'park')
        block159 = Block(2840, 480, 'park')
        block160 = Block(3000, 480, 'park')
        block161 = Block(3800, 480, 'park')
        block162 = Block(4080, 480, 'park')
        block163 = Block(280, 520, 'park')
        block164 = Block(360, 520, 'park')
        block165 = Block(1320, 520, 'park')
        block166 = Block(1440, 520, 'park')
        block167 = Block(2280, 520, 'park')
        block168 = Block(2440, 520, 'park')
        block169 = Block(3000, 520, 'park')
        block170 = Block(4120, 520, 'park')
        block171 = Block(0, 560, 'park')
        block172 = Block(40, 560, 'park')
        block173 = Block(80, 560, 'park')
        block174 = Block(120, 560, 'park')
        block175 = Block(160, 560, 'park')
        block176 = Block(200, 560, 'park')
        block177 = Block(240, 560, 'park')
        block178 = Block(280, 560, 'park')
        block179 = Block(320, 560, 'park')
        block180 = Block(360, 560, 'park')
        block181 = Block(400, 560, 'park')
        block182 = Block(440, 560, 'park')
        block183 = Block(480, 560, 'park')
        block184 = Block(520, 560, 'park')
        block185 = Block(560, 560, 'park')
        block186 = Block(600, 560, 'park')
        block187 = Block(640, 560, 'park')
        block188 = Block(680, 560, 'park')
        block189 = Block(720, 560, 'park')
        block190 = Block(760, 560, 'park')
        block191 = Block(800, 560, 'park')
        block192 = Block(840, 560, 'park')
        block193 = Block(880, 560, 'park')
        block194 = Block(920, 560, 'park')
        block195 = Block(960, 560, 'park')
        block196 = Block(1000, 560, 'park')
        block197 = Block(1040, 560, 'park')
        block198 = Block(1080, 560, 'park')
        block199 = Block(1120, 560, 'park')
        block200 = Block(1160, 560, 'park')
        block201 = Block(1200, 560, 'park')
        block202 = Block(1240, 560, 'park')
        block203 = Block(1280, 560, 'park')
        block204 = Block(1320, 560, 'park')
        block205 = Block(1360, 560, 'park')
        block206 = Block(1400, 560, 'park')
        block207 = Block(1440, 560, 'park')
        block208 = Block(1480, 560, 'park')
        block209 = Block(1520, 560, 'park')
        block210 = Block(1560, 560, 'park')
        block211 = Block(1600, 560, 'park')
        block212 = Block(1640, 560, 'park')
        block213 = Block(1680, 560, 'park')
        block214 = Block(1720, 560, 'park')
        block215 = Block(1760, 560, 'park')
        block216 = Block(1800, 560, 'park')
        block217 = Block(1840, 560, 'park')
        block218 = Block(1880, 560, 'park')
        block219 = Block(1920, 560, 'park')
        block220 = Block(1960, 560, 'park')
        block221 = Block(2000, 560, 'park')
        block222 = Block(2040, 560, 'park')
        block223 = Block(2080, 560, 'park')
        block224 = Block(2120, 560, 'park')
        block225 = Block(2160, 560, 'park')
        block226 = Block(2200, 560, 'park')
        block227 = Block(2240, 560, 'park')
        block228 = Block(2280, 560, 'park')
        block229 = Block(2320, 560, 'park')
        block230 = Block(2360, 560, 'park')
        block231 = Block(2400, 560, 'park')
        block232 = Block(2440, 560, 'park')
        block233 = Block(2480, 560, 'park')
        block234 = Block(2520, 560, 'park')
        block235 = Block(2560, 560, 'park')
        block236 = Block(2600, 560, 'park')
        block237 = Block(2640, 560, 'park')
        block238 = Block(2680, 560, 'park')
        block239 = Block(2720, 560, 'park')
        block240 = Block(2760, 560, 'park')
        block241 = Block(2800, 560, 'park')
        block242 = Block(2840, 560, 'park')
        block243 = Block(2880, 560, 'park')
        block244 = Block(2920, 560, 'park')
        block245 = Block(2960, 560, 'park')
        block246 = Block(3000, 560, 'park')
        block247 = Block(3040, 560, 'park')
        block248 = Block(3080, 560, 'park')
        block249 = Block(3120, 560, 'park')
        block250 = Block(3160, 560, 'park')
        block251 = Block(3200, 560, 'park')
        block252 = Block(3240, 560, 'park')
        block253 = Block(3280, 560, 'park')
        block254 = Block(3320, 560, 'park')
        block255 = Block(3360, 560, 'park')
        block256 = Block(3400, 560, 'park')
        block257 = Block(3440, 560, 'park')
        block258 = Block(3480, 560, 'park')
        block259 = Block(3520, 560, 'park')
        block260 = Block(3560, 560, 'park')
        block261 = Block(3600, 560, 'park')
        block262 = Block(3640, 560, 'park')
        block263 = Block(3680, 560, 'park')
        block264 = Block(3720, 560, 'park')
        block265 = Block(3760, 560, 'park')
        block266 = Block(3800, 560, 'park')
        block267 = Block(3840, 560, 'park')
        block268 = Block(3880, 560, 'park')
        block269 = Block(3920, 560, 'park')
        block270 = Block(3960, 560, 'park')
        block271 = Block(4000, 560, 'park')
        block272 = Block(4040, 560, 'park')
        block273 = Block(4080, 560, 'park')
        block274 = Block(4120, 560, 'park')
        block275 = Block(4160, 560, 'park')
        block276 = Block(4200, 560, 'park')
        block277 = Block(4240, 560, 'park')
        block278 = Block(4280, 560, 'park')
        block279 = Block(4320, 560, 'park')
        block280 = Block(4360, 560, 'park')
        block281 = Block(4400, 560, 'park')
        block282 = Block(4440, 560, 'park')
        block283 = Block(4480, 560, 'park')
        block284 = Block(4520, 560, 'park')
        block285 = Block(4560, 560, 'park')
        block286 = Block(4600, 560, 'park')
        block287 = Block(4640, 560, 'park')
        block288 = Block(4680, 560, 'park')
        block289 = Block(4720, 560, 'park')
        block290 = Block(4760, 560, 'park')
        block291 = Block(4800, 560, 'park')
        block292 = Block(4840, 560, 'park')
        block293 = Block(4880, 560, 'park')
        block294 = Block(4920, 560, 'park')
        block295 = Block(4960, 560, 'park')

        self.blocks = pygame.sprite.Group(block0, block1, block2, block3,
                                            block4, block5, block6, block7,
                                            block8, block9, block10, block11,
                                            block12, block13, block14, block15,
                                            block16, block17, block18, block19,
                                            block20, block21, block22, block23,
                                            block24, block25, block26, block27,
                                            block28, block29, block30, block31,
                                            block32, block33, block34, block35,
                                            block36, block37, block38, block39,
                                            block40, block41, block42, block43,
                                            block44, block45, block46, block47,
                                            block48, block49, block50, block51,
                                            block52, block53, block54, block55,
                                            block56, block57, block58, block59,
                                            block60, block61, block62, block63,
                                            block64, block65, block66, block67,
                                            block68, block69, block70, block71,
                                            block72, block73, block74, block75,
                                            block76, block77, block78, block79,
                                            block80, block81, block82, block83,
                                            block84, block85, block86, block87,
                                            block88, block89, block90, block91,
                                            block92, block93, block94, block95,
                                            block96, block97, block98, block99,
                                            block100, block101, block102, block103,
                                            block104, block105, block106, block107,
                                            block108, block109, block110, block111,
                                            block112, block113, block114, block115,
                                            block116, block117, block118, block119,
                                            block120, block121, block122, block123,
                                            block124, block125, block126, block127,
                                            block128, block129, block130, block131,
                                            block132, block133, block134, block135,
                                            block136, block137, block138, block139,
                                            block140, block141, block142, block143,
                                            block144, block145, block146, block147,
                                            block148, block149, block150, block151,
                                            block152, block153, block154, block155,
                                            block156, block157, block158, block159,
                                            block160, block161, block162, block163,
                                            block164, block165, block166, block167,
                                            block168, block169, block170, block171,
                                            block172, block173, block174, block175,
                                            block176, block177, block178, block179,
                                            block180, block181, block182, block183,
                                            block184, block185, block186, block187,
                                            block188, block189, block190, block191,
                                            block192, block193, block194, block195,
                                            block196, block197, block198, block199,
                                            block200, block201, block202, block203,
                                            block204, block205, block206, block207,
                                            block208, block209, block210, block211,
                                            block212, block213, block214, block215,
                                            block216, block217, block218, block219,
                                            block220, block221, block222, block223,
                                            block224, block225, block226, block227,
                                            block228, block229, block230, block231,
                                            block232, block233, block234, block235,
                                            block236, block237, block238, block239,
                                            block240, block241, block242, block243,
                                            block244, block245, block246, block247,
                                            block248, block249, block250, block251,
                                            block252, block253, block254, block255,
                                            block256, block257, block258, block259,
                                            block260, block261, block262, block263,
                                            block264, block265, block266, block267,
                                            block268, block269, block270, block271,
                                            block272, block273, block274, block275,
                                            block276, block277, block278, block279,
                                            block280, block281, block282, block283,
                                            block284, block285, block286, block287,
                                            block288, block289, block290, block291,
                                            block292, block293, block294, block295)
        

    def set_enemies(self):
        bear0 = enemies.Bear(2960, 160)
        bear_group0 = pygame.sprite.Group(bear0)
        bear1 = enemies.Bear(3200, 160)
        bear_group1 = pygame.sprite.Group(bear1)
        bear2 = enemies.Bear(400, 200)
        bear_group2 = pygame.sprite.Group(bear2)
        bear3 = enemies.Bear(1800, 360)
        bear_group3 = pygame.sprite.Group(bear3)
        bear4 = enemies.Bear(3960, 400)
        bear_group4 = pygame.sprite.Group(bear4)
        bear5 = enemies.Bear(680, 480)
        bear_group5 = pygame.sprite.Group(bear5)
        bear6 = enemies.Bear(2080, 560)
        bear_group6 = pygame.sprite.Group(bear6)
        clown0 = enemies.Clown(1880, 160)
        clown_group0 = pygame.sprite.Group(clown0)
        clown1 = enemies.Clown(3240, 360)
        clown_group1 = pygame.sprite.Group(clown1)
        clown2 = enemies.Clown(920, 560)
        clown_group2 = pygame.sprite.Group(clown2)
        clown3 = enemies.Clown(1240, 560)
        clown_group3 = pygame.sprite.Group(clown3)
        clown4 = enemies.Clown(1560, 560)
        clown_group4 = pygame.sprite.Group(clown4)
        clown5 = enemies.Clown(2640, 560)
        clown_group5 = pygame.sprite.Group(clown5)
        clown6 = enemies.Clown(3200, 560)
        clown_group6 = pygame.sprite.Group(clown6)
        clown7 = enemies.Clown(3240, 560)
        clown_group7 = pygame.sprite.Group(clown7)
        self.enemy_group_list = [bear_group0, bear_group1, bear_group2, bear_group3,
                                bear_group4, bear_group5, bear_group6,
                                clown_group0, clown_group1, clown_group2, clown_group3,
                                clown_group4, clown_group5, clown_group6, clown_group7]

    def set_checkpoints(self):
        check1 = checkpoint.Checkpoint(1960, "1")
        check2 = checkpoint.Checkpoint(2200, '2')
        check3 = checkpoint.Checkpoint(110, '3')
        check4 = checkpoint.Checkpoint(800, "4")
        check5 = checkpoint.Checkpoint(1960, '5')
        check6 = checkpoint.Checkpoint(110, '6')
        check7 = checkpoint.Checkpoint(1080, '7')
        check8 = checkpoint.Checkpoint(880, "8")
        check9 = checkpoint.Checkpoint(2240, '9')
        check10 = checkpoint.Checkpoint(110, '10')
        check11 = checkpoint.Checkpoint(240, "11")
        check12 = checkpoint.Checkpoint(5600, '12')
        check13 = checkpoint.Checkpoint(1640, '13')
        check14 = checkpoint.Checkpoint(2200, '14')
        check15 = checkpoint.Checkpoint(2240, '15')
        self.check_point_group = pygame.sprite.Group(check1, check2, check3, check4,
                                                     check5, check6, check7, check8,
                                                     check9, check10, check11,
                                                     check12, check13, check14, check15)


    def set_spritegroups(self):
        self.enemy_group = pygame.sprite.Group()
        self.hero_and_enemy_group = pygame.sprite.Group(self.hero,
                                                     self.enemy_group)


    def on_update(self, keys):
        self.update_everything(keys)
        self.blit_everything()
        self.update_viewport()


    def update_everything(self, keys):
        self.hero.update(keys, {})
        self.info_coin.rect.x = self.viewport.x + 1000 - self.info_coin.w
        self.check_cp()
        self.sprite_positions()
        self.info_coin.update()
        self.end_of_level()
        self.enemy_group.update(keys)


    def end_of_level(self):
        if self.hero.rect.x >= 4900:
            self.done = True

    def sprite_positions(self):
        self.hero_position()

        
    def hero_position(self):
        self.last_x_position = self.hero.rect.right
        self.hero.rect.x += round(self.hero.x_vel)
        self.x_collisions_hero()

        self.hero.rect.y += round(self.hero.y_vel)
        self.y_collisions_hero()

        if self.hero.rect.x < (self.viewport.x + 5):
            self.hero.rect.x = (self.viewport.x + 5)


    def x_collisions_hero(self):
        bricks = pygame.sprite.spritecollideany(self.hero, self.blocks)
        enemy = pygame.sprite.spritecollideany(self.hero, self.enemy_group)
        coin = pygame.sprite.spritecollideany(self.hero, self.coins)
        
        if bricks:
            self.x_collisions_solve(bricks)

        if enemy:
            if self.hero.flag == True:
                enemy.kill()
            else:
                self.x_collisions_solve(enemy)

        if coin:
            self.info_coin.number += 1
            coin.kill()


    def x_collisions_solve(self, collider):
        self.hero.x_vel = 0
        if self.hero.rect.x < collider.rect.x:
            self.hero.rect.right = collider.rect.left
        else:
            self.hero.rect.left = collider.rect.right


    def y_collisions_hero(self):
        bricks = pygame.sprite.spritecollideany(self.hero, self.blocks)
        
        if bricks:
            if self.hero.rect.y > bricks.rect.y:
                self.hero.rect.y = bricks.rect.bottom
                self.hero.y_vel = 7
                self.hero.state = "FALL"
            else:
                self.hero.rect.bottom = bricks.rect.top
                self.hero.y_vel = 0
                self.hero.state = "WALK"


        self.hero.rect.y += 1

        if not pygame.sprite.spritecollideany(self.hero, self.blocks):
            if self.hero.state != "JUMP":
                self.hero.state = "FALL"

        self.hero.rect.y -= 1



        
    def blit_everything(self):
        pygame.display.flip()
        self.level.blit(self.background, self.viewport, self.viewport)
        self.blocks.draw(self.level)
        self.hero_and_enemy_group.draw(self.level)
        self.coins.draw(self.level)
        self.info.draw(self.level)
        screen.blit(self.level, (0,0), self.viewport)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));

    def check_cp(self):
        ''' check check points'''
        checkpoint = pygame.sprite.spritecollideany(self.hero, self.check_point_group)
        if checkpoint:
            checkpoint.kill()
            for i in range(1,16):
                if checkpoint.name == str(i):
                    self.enemy_group.add(self.enemy_group_list[i-1])
            self.hero_and_enemy_group.add(self.enemy_group)
    
    
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True


    def update_viewport(self):
        if (self.viewport.x <= 4000):
            third = self.viewport.x + self.viewport.w//3
            play_center = self.hero.rect.centerx
            play_right = self.hero.rect.right

            if self.hero.x_vel > 0 and play_center >= third:
                mult = 1 if play_right < self.viewport.centerx else 2
                new = self.viewport.x + mult * self.hero.x_vel
                highest = self.level_rect.w - self.viewport.w
                self.viewport.x = min(highest, new)

