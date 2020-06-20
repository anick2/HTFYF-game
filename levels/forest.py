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
        coin0 = Coin(1360, 80)
        coin1 = Coin(1400, 80)
        coin2 = Coin(2080, 80)
        coin3 = Coin(3840, 160)
        coin4 = Coin(3600, 280)
        coin5 = Coin(2640, 320)
        coin6 = Coin(3240, 320)
        coin7 = Coin(1000, 360)
        coin8 = Coin(1240, 360)
        coin9 = Coin(80, 400)
        coin10 = Coin(720, 400)
        coin11 = Coin(360, 440)
        coin12 = Coin(2960, 440)
        coin13 = Coin(520, 520)
        coin14 = Coin(960, 520)
        coin15 = Coin(1280, 520)
        coin16 = Coin(1880, 520)
        coin17 = Coin(2400, 520)
        coin18 = Coin(3280, 520)
        coin19 = Coin(3960, 520)
        self.coins = pygame.sprite.Group(coin0, coin1, coin2, coin3,
                                        coin4, coin5, coin6, coin7,
                                        coin8, coin9, coin10, coin11,
                                        coin12, coin13, coin14, coin15,
                                        coin16, coin17, coin18, coin19)

    def set_blocks(self):
        #self.ground = Barrier(0, c.HEIGHT_OF_GROUND, 3000, 40)

        block0 = Block(1360, 120, 'forest')
        block1 = Block(1400, 120, 'forest')
        block2 = Block(1440, 160, 'forest')
        block3 = Block(1480, 200, 'forest')
        block4 = Block(1520, 240, 'forest')
        block5 = Block(1560, 240, 'forest')
        block6 = Block(1600, 240, 'forest')
        block7 = Block(1640, 240, 'forest')
        block8 = Block(1680, 240, 'forest')
        block9 = Block(1720, 240, 'forest')
        block10 = Block(1760, 240, 'forest')
        block11 = Block(1920, 240, 'forest')
        block12 = Block(1960, 240, 'forest')
        block13 = Block(2000, 240, 'forest')
        block14 = Block(2040, 240, 'forest')
        block15 = Block(2080, 240, 'forest')
        block16 = Block(2120, 240, 'forest')
        block17 = Block(2160, 240, 'forest')
        block18 = Block(2200, 240, 'forest')
        block19 = Block(1880, 280, 'forest')
        block20 = Block(1920, 280, 'forest')
        block21 = Block(1960, 280, 'forest')
        block22 = Block(2000, 280, 'forest')
        block23 = Block(2040, 280, 'forest')
        block24 = Block(2080, 280, 'forest')
        block25 = Block(2120, 280, 'forest')
        block26 = Block(2160, 280, 'forest')
        block27 = Block(2200, 280, 'forest')
        block28 = Block(3800, 280, 'forest')
        block29 = Block(3880, 280, 'forest')
        block30 = Block(1840, 320, 'forest')
        block31 = Block(1880, 320, 'forest')
        block32 = Block(1920, 320, 'forest')
        block33 = Block(2960, 320, 'forest')
        block34 = Block(3760, 320, 'forest')
        block35 = Block(3800, 320, 'forest')
        block36 = Block(3840, 320, 'forest')
        block37 = Block(3880, 320, 'forest')
        block38 = Block(3920, 320, 'forest')
        block39 = Block(240, 360, 'forest')
        block40 = Block(1800, 360, 'forest')
        block41 = Block(1840, 360, 'forest')
        block42 = Block(1880, 360, 'forest')
        block43 = Block(2960, 360, 'forest')
        block44 = Block(3240, 360, 'forest')
        block45 = Block(3720, 360, 'forest')
        block46 = Block(3760, 360, 'forest')
        block47 = Block(3800, 360, 'forest')
        block48 = Block(3840, 360, 'forest')
        block49 = Block(3880, 360, 'forest')
        block50 = Block(3920, 360, 'forest')
        block51 = Block(1760, 400, 'forest')
        block52 = Block(1800, 400, 'forest')
        block53 = Block(1840, 400, 'forest')
        block54 = Block(2760, 400, 'forest')
        block55 = Block(2800, 400, 'forest')
        block56 = Block(2840, 400, 'forest')
        block57 = Block(2880, 400, 'forest')
        block58 = Block(2920, 400, 'forest')
        block59 = Block(2960, 400, 'forest')
        block60 = Block(3000, 400, 'forest')
        block61 = Block(3040, 400, 'forest')
        block62 = Block(3080, 400, 'forest')
        block63 = Block(3120, 400, 'forest')
        block64 = Block(3160, 400, 'forest')
        block65 = Block(3200, 400, 'forest')
        block66 = Block(3240, 400, 'forest')
        block67 = Block(3680, 400, 'forest')
        block68 = Block(3720, 400, 'forest')
        block69 = Block(3760, 400, 'forest')
        block70 = Block(3800, 400, 'forest')
        block71 = Block(3840, 400, 'forest')
        block72 = Block(3880, 400, 'forest')
        block73 = Block(3920, 400, 'forest')
        block74 = Block(1640, 440, 'forest')
        block75 = Block(1680, 440, 'forest')
        block76 = Block(1720, 440, 'forest')
        block77 = Block(1760, 440, 'forest')
        block78 = Block(1800, 440, 'forest')
        block79 = Block(2600, 440, 'forest')
        block80 = Block(2640, 440, 'forest')
        block81 = Block(2680, 440, 'forest')
        block82 = Block(2720, 440, 'forest')
        block83 = Block(2760, 440, 'forest')
        block84 = Block(2800, 440, 'forest')
        block85 = Block(2840, 440, 'forest')
        block86 = Block(3120, 440, 'forest')
        block87 = Block(3160, 440, 'forest')
        block88 = Block(3200, 440, 'forest')
        block89 = Block(3240, 440, 'forest')
        block90 = Block(3640, 440, 'forest')
        block91 = Block(3680, 440, 'forest')
        block92 = Block(3720, 440, 'forest')
        block93 = Block(3760, 440, 'forest')
        block94 = Block(3800, 440, 'forest')
        block95 = Block(3840, 440, 'forest')
        block96 = Block(3880, 440, 'forest')
        block97 = Block(3920, 440, 'forest')
        block98 = Block(320, 480, 'forest')
        block99 = Block(360, 480, 'forest')
        block100 = Block(400, 480, 'forest')
        block101 = Block(840, 480, 'forest')
        block102 = Block(920, 480, 'forest')
        block103 = Block(1000, 480, 'forest')
        block104 = Block(1240, 480, 'forest')
        block105 = Block(1520, 480, 'forest')
        block106 = Block(1560, 480, 'forest')
        block107 = Block(1600, 480, 'forest')
        block108 = Block(1640, 480, 'forest')
        block109 = Block(1680, 480, 'forest')
        block110 = Block(1720, 480, 'forest')
        block111 = Block(1760, 480, 'forest')
        block112 = Block(2560, 480, 'forest')
        block113 = Block(2600, 480, 'forest')
        block114 = Block(2640, 480, 'forest')
        block115 = Block(2680, 480, 'forest')
        block116 = Block(2720, 480, 'forest')
        block117 = Block(2760, 480, 'forest')
        block118 = Block(2800, 480, 'forest')
        block119 = Block(2840, 480, 'forest')
        block120 = Block(3600, 480, 'forest')
        block121 = Block(3640, 480, 'forest')
        block122 = Block(3680, 480, 'forest')
        block123 = Block(3720, 480, 'forest')
        block124 = Block(3760, 480, 'forest')
        block125 = Block(3800, 480, 'forest')
        block126 = Block(3840, 480, 'forest')
        block127 = Block(3880, 480, 'forest')
        block128 = Block(3920, 480, 'forest')
        block129 = Block(4000, 480, 'forest')
        block130 = Block(4320, 480, 'forest')
        block131 = Block(280, 520, 'forest')
        block132 = Block(320, 520, 'forest')
        block133 = Block(360, 520, 'forest')
        block134 = Block(400, 520, 'forest')
        block135 = Block(560, 520, 'forest')
        block136 = Block(600, 520, 'forest')
        block137 = Block(640, 520, 'forest')
        block138 = Block(680, 520, 'forest')
        block139 = Block(720, 520, 'forest')
        block140 = Block(840, 520, 'forest')
        block141 = Block(920, 520, 'forest')
        block142 = Block(1000, 520, 'forest')
        block143 = Block(1240, 520, 'forest')
        block144 = Block(1480, 520, 'forest')
        block145 = Block(1520, 520, 'forest')
        block146 = Block(1560, 520, 'forest')
        block147 = Block(1600, 520, 'forest')
        block148 = Block(1640, 520, 'forest')
        block149 = Block(1680, 520, 'forest')
        block150 = Block(1720, 520, 'forest')
        block151 = Block(1760, 520, 'forest')
        block152 = Block(2360, 520, 'forest')
        block153 = Block(2520, 520, 'forest')
        block154 = Block(2560, 520, 'forest')
        block155 = Block(2600, 520, 'forest')
        block156 = Block(2640, 520, 'forest')
        block157 = Block(2680, 520, 'forest')
        block158 = Block(2720, 520, 'forest')
        block159 = Block(2760, 520, 'forest')
        block160 = Block(2800, 520, 'forest')
        block161 = Block(2840, 520, 'forest')
        block162 = Block(3560, 520, 'forest')
        block163 = Block(3600, 520, 'forest')
        block164 = Block(3640, 520, 'forest')
        block165 = Block(3680, 520, 'forest')
        block166 = Block(3720, 520, 'forest')
        block167 = Block(3760, 520, 'forest')
        block168 = Block(3800, 520, 'forest')
        block169 = Block(3840, 520, 'forest')
        block170 = Block(3880, 520, 'forest')
        block171 = Block(3920, 520, 'forest')
        block172 = Block(4000, 520, 'forest')
        block173 = Block(4040, 520, 'forest')
        block174 = Block(4160, 520, 'forest')
        block175 = Block(4320, 520, 'forest')
        block176 = Block(0, 560, 'forest')
        block177 = Block(40, 560, 'forest')
        block178 = Block(80, 560, 'forest')
        block179 = Block(120, 560, 'forest')
        block180 = Block(160, 560, 'forest')
        block181 = Block(200, 560, 'forest')
        block182 = Block(240, 560, 'forest')
        block183 = Block(280, 560, 'forest')
        block184 = Block(320, 560, 'forest')
        block185 = Block(360, 560, 'forest')
        block186 = Block(400, 560, 'forest')
        block187 = Block(440, 560, 'forest')
        block188 = Block(480, 560, 'forest')
        block189 = Block(520, 560, 'forest')
        block190 = Block(560, 560, 'forest')
        block191 = Block(600, 560, 'forest')
        block192 = Block(640, 560, 'forest')
        block193 = Block(680, 560, 'forest')
        block194 = Block(720, 560, 'forest')
        block195 = Block(760, 560, 'forest')
        block196 = Block(800, 560, 'forest')
        block197 = Block(840, 560, 'forest')
        block198 = Block(880, 560, 'forest')
        block199 = Block(920, 560, 'forest')
        block200 = Block(960, 560, 'forest')
        block201 = Block(1000, 560, 'forest')
        block202 = Block(1040, 560, 'forest')
        block203 = Block(1080, 560, 'forest')
        block204 = Block(1120, 560, 'forest')
        block205 = Block(1160, 560, 'forest')
        block206 = Block(1200, 560, 'forest')
        block207 = Block(1240, 560, 'forest')
        block208 = Block(1280, 560, 'forest')
        block209 = Block(1320, 560, 'forest')
        block210 = Block(1360, 560, 'forest')
        block211 = Block(1400, 560, 'forest')
        block212 = Block(1440, 560, 'forest')
        block213 = Block(1480, 560, 'forest')
        block214 = Block(1520, 560, 'forest')
        block215 = Block(1560, 560, 'forest')
        block216 = Block(1600, 560, 'forest')
        block217 = Block(1640, 560, 'forest')
        block218 = Block(1680, 560, 'forest')
        block219 = Block(1720, 560, 'forest')
        block220 = Block(1760, 560, 'forest')
        block221 = Block(1800, 560, 'forest')
        block222 = Block(1840, 560, 'forest')
        block223 = Block(1880, 560, 'forest')
        block224 = Block(1920, 560, 'forest')
        block225 = Block(1960, 560, 'forest')
        block226 = Block(2000, 560, 'forest')
        block227 = Block(2040, 560, 'forest')
        block228 = Block(2080, 560, 'forest')
        block229 = Block(2120, 560, 'forest')
        block230 = Block(2160, 560, 'forest')
        block231 = Block(2200, 560, 'forest')
        block232 = Block(2240, 560, 'forest')
        block233 = Block(2280, 560, 'forest')
        block234 = Block(2320, 560, 'forest')
        block235 = Block(2360, 560, 'forest')
        block236 = Block(2400, 560, 'forest')
        block237 = Block(2440, 560, 'forest')
        block238 = Block(2480, 560, 'forest')
        block239 = Block(2520, 560, 'forest')
        block240 = Block(2560, 560, 'forest')
        block241 = Block(2600, 560, 'forest')
        block242 = Block(2640, 560, 'forest')
        block243 = Block(2680, 560, 'forest')
        block244 = Block(2720, 560, 'forest')
        block245 = Block(2760, 560, 'forest')
        block246 = Block(2800, 560, 'forest')
        block247 = Block(2840, 560, 'forest')
        block248 = Block(2880, 560, 'forest')
        block249 = Block(2920, 560, 'forest')
        block250 = Block(2960, 560, 'forest')
        block251 = Block(3000, 560, 'forest')
        block252 = Block(3040, 560, 'forest')
        block253 = Block(3080, 560, 'forest')
        block254 = Block(3120, 560, 'forest')
        block255 = Block(3160, 560, 'forest')
        block256 = Block(3200, 560, 'forest')
        block257 = Block(3240, 560, 'forest')
        block258 = Block(3280, 560, 'forest')
        block259 = Block(3320, 560, 'forest')
        block260 = Block(3360, 560, 'forest')
        block261 = Block(3400, 560, 'forest')
        block262 = Block(3440, 560, 'forest')
        block263 = Block(3480, 560, 'forest')
        block264 = Block(3520, 560, 'forest')
        block265 = Block(3560, 560, 'forest')
        block266 = Block(3600, 560, 'forest')
        block267 = Block(3640, 560, 'forest')
        block268 = Block(3680, 560, 'forest')
        block269 = Block(3720, 560, 'forest')
        block270 = Block(3760, 560, 'forest')
        block271 = Block(3800, 560, 'forest')
        block272 = Block(3840, 560, 'forest')
        block273 = Block(3880, 560, 'forest')
        block274 = Block(3920, 560, 'forest')
        block275 = Block(3960, 560, 'forest')
        block276 = Block(4000, 560, 'forest')
        block277 = Block(4040, 560, 'forest')
        block278 = Block(4080, 560, 'forest')
        block279 = Block(4120, 560, 'forest')
        block280 = Block(4160, 560, 'forest')
        block281 = Block(4200, 560, 'forest')
        block282 = Block(4240, 560, 'forest')
        block283 = Block(4280, 560, 'forest')
        block284 = Block(4320, 560, 'forest')
        block285 = Block(4360, 560, 'forest')
        block286 = Block(4400, 560, 'forest')
        block287 = Block(4440, 560, 'forest')
        block288 = Block(4480, 560, 'forest')
        block289 = Block(4520, 560, 'forest')
        block290 = Block(4560, 560, 'forest')
        block291 = Block(4600, 560, 'forest')
        block292 = Block(4640, 560, 'forest')
        block293 = Block(4680, 560, 'forest')
        block294 = Block(4720, 560, 'forest')
        block295 = Block(4760, 560, 'forest')
        block296 = Block(4800, 560, 'forest')
        block297 = Block(4840, 560, 'forest')
        block298 = Block(4880, 560, 'forest')
        block299 = Block(4920, 560, 'forest')
        block300 = Block(4960, 560, 'forest')

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
                                        block292, block293, block294, block295,
                                        block296, block297, block298, block299,
                                        block300)
        

    def set_enemies(self):
        mushroom0 = enemies.Mushroom(3840, 320)
        mushroom_group0 = pygame.sprite.Group(mushroom0)
        mushroom1 = enemies.Mushroom(3000, 400)
        mushroom_group1 = pygame.sprite.Group(mushroom1)
        mushroom2 = enemies.Mushroom(1560, 480)
        mushroom_group2 = pygame.sprite.Group(mushroom2)
        mushroom3 = enemies.Mushroom(2560, 480)
        mushroom_group3 = pygame.sprite.Group(mushroom3)
        mushroom4 = enemies.Mushroom(440, 560)
        mushroom_group4 = pygame.sprite.Group(mushroom4)
        mushroom5 = enemies.Mushroom(1800, 560)
        mushroom_group5 = pygame.sprite.Group(mushroom5)
        mushroom6 = enemies.Mushroom(4240, 560)
        mushroom_group6 = pygame.sprite.Group(mushroom6)
        spider0 = enemies.Spider(1560, 240)
        spider_group0 = pygame.sprite.Group(spider0)
        spider1 = enemies.Spider(2120, 240)
        spider_group1 = pygame.sprite.Group(spider1)
        spider2 = enemies.Spider(600, 520)
        spider_group2 = pygame.sprite.Group(spider2)
        spider3 = enemies.Spider(1160, 560)
        spider_group3 = pygame.sprite.Group(spider3)
        spider4 = enemies.Spider(2000, 560)
        spider_group4 = pygame.sprite.Group(spider4)
        spider5 = enemies.Spider(3000, 560)
        spider_group5 = pygame.sprite.Group(spider5)
        spider6 = enemies.Spider(4120, 560)
        spider_group6 = pygame.sprite.Group(spider6)
        self.enemies = [mushroom0,mushroom1,mushroom2,mushroom3,mushroom4,mushroom5,mushroom6,spider1,spider2,spider3,spider4,spider5,spider6]
        self.enemy_group_list = [mushroom_group0, mushroom_group1, mushroom_group2, mushroom_group3,
                                 mushroom_group4, mushroom_group5, mushroom_group6, spider_group0,
                                 spider_group1, spider_group2, spider_group3, spider_group4,
                                 spider_group5, spider_group6]


    def set_checkpoints(self):
        check1 = checkpoint.Checkpoint(110, "1")
        check2 = checkpoint.Checkpoint(2000, '2')
        check3 = checkpoint.Checkpoint(560, '3')
        check4 = checkpoint.Checkpoint(1560, "4")
        check5 = checkpoint.Checkpoint(110, '5')
        check6 = checkpoint.Checkpoint(110, '6')
        check7 = checkpoint.Checkpoint(3240, '7')
        check8 = checkpoint.Checkpoint(560, "8")
        check9 = checkpoint.Checkpoint(1120, '9')
        check10 = checkpoint.Checkpoint(110, '10')
        check11 = checkpoint.Checkpoint(160, "11")
        check12 = checkpoint.Checkpoint(1000, '12')
        check13 = checkpoint.Checkpoint(2000, '13')
        check14 = checkpoint.Checkpoint(3120, '14')
        self.check_point_group = pygame.sprite.Group(check1, check2, check3, check4,
                                                     check5, check6, check7, check8,
                                                     check9, check10, check11,
                                                     check12, check13, check14)

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
        self.info_coin.update()
        for i in self.enemy_group:
            i.update(keys)
        self.sprite_positions()
        self.coins.update()
        self.end_of_level()


    def end_of_level(self):
        if self.hero.rect.x >= 4900:
            self.done = True

    def sprite_positions(self):
        self.hero_position()
        self.enemy_position()

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

    def enemy_position(self):
        for i in self.enemies:
            self.last_x_position = i.rect.right
            if i.direction == 'right':
                i.rect.x += round(i.x_vel)
            else:
                i.rect.x -= round(i.x_vel)
            self.x_collisions_enemy(i)
            self.y_collisions_enemy(i)

    def x_collisions_enemy(self, i):
        bricks = pygame.sprite.spritecollideany(i, self.blocks)
        enemy = pygame.sprite.spritecollideany(self.hero, self.enemy_group)
        #coin = pygame.sprite.spritecollideany(self.enemy_group, self.coins)
        
        if bricks:
            self.x_collisions_solve_enemy(bricks, i)
        if enemy:
            self.x_collisions_solve_enemy(self.hero, enemy)

    def x_collisions_solve_enemy(self, collider, i):
        if i.direction == 'right':
            i.direction = 'left'
        else:
            i.direction = 'right'
        if i.rect.x < collider.rect.x:
            i.rect.right = collider.rect.left
        else:
            i.rect.left = collider.rect.right


    def y_collisions_enemy(self, i):
        """Проверяет наличие столкновений, когда враг движется вдоль оси Y"""
        bricks = pygame.sprite.spritecollideany(i, self.blocks)
        if bricks:
            print(i.rect.y, bricks.rect.y)
            if i.rect.y > bricks.rect.y:
                i.rect.y = bricks.rect.bottom
                i.y_vel = 0
                i.state = "FALL"
            else:
                i.rect.bottom = bricks.rect.top
                i.y_vel = 0
                i.state = "WALK"
        else:
            i.rect.y += 1
            if not pygame.sprite.spritecollideany(i, self.blocks):
                i.state = "WALK"
                if i.direction == 'right':
                    i.direction = 'left'
                else:
                    i.direction = 'right'
            i.rect.y -= 1

    def blit_everything(self):
        pygame.display.flip()
        self.level.blit(self.background, self.viewport, self.viewport)
        self.coins.draw(self.level)
        self.info.draw(self.level)
        self.blocks.draw(self.level)
        self.pers.draw(self.level)
        self.hero_and_enemy_group.draw(self.level)
        screen.blit(self.level, (0,0), self.viewport)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));
        

    def check_cp(self):
        ''' check check points'''
        checkpoint = pygame.sprite.spritecollideany(self.hero, self.check_point_group)
        if checkpoint:
            checkpoint.kill()
            for i in range(1,15):
                if checkpoint.name == str(i):
                    #for index, enemy in enumerate(self.enemy_group_list[i - 1]):
                        #enemy.rect.x = self.viewport.right + (index * 60)
                        #enemy.rect.bottom = 560
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
