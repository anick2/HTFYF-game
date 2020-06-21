import sys
import pygame
from .state import State
from init import screen, IMAGES
import hero
import enemies
import checkpoint
from sprites import Block, Coin, Info_coin, Info_hearts, Heal
from sounds import Sound

sys.path.append('..')


class City(State):
    """Класс для состояния город"""
    def __init__(self):
        State.__init__(self)
        self.next_state = "PARK"

    def set_background(self):
        """Устанавливает фоновое изображение,
           прямоугольник и масштабирует его до правильного размера"""
        self.background = IMAGES['city']
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height
        self.level = pygame.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = screen.get_rect(bottom=self.level_rect.bottom)
        self.level.blit(self.background, (0, 0))
        screen.blit(self.level, (0, 0), self.viewport)

    def on_create(self):
        """Вызывается при создании объекта"""
        self.sound_player = Sound("CITY")
        self.set_background()
        self.set_hero()
        self.set_blocks()
        self.set_enemies()
        self.set_coins()
        self.set_healing()
        self.set_checkpoints()
        self.set_spritegroups()

    def set_healing(self):
        bottle1 = Heal(1920, 100)
        self.healing = pygame.sprite.Group(bottle1)

    def set_hero(self):
        """Создание героя"""
        self.hero = hero.Hero()
        self.hero.rect.x = self.viewport.x + 110
        self.hero.rect.bottom = 560
        self.pers = pygame.sprite.Group(self.hero)
        self.info_coin = Info_coin()
        self.info_hearts = Info_hearts()
        self.info = pygame.sprite.Group(self.info_coin, self.info_hearts)

    def set_coins(self):
        """Создает все монетки для уровня"""
        coin0 = Coin(680, 40)
        coin1 = Coin(1920, 80)
        coin2 = Coin(2080, 80)
        coin3 = Coin(3080, 80)
        coin4 = Coin(3120, 80)
        coin5 = Coin(2840, 120)
        coin6 = Coin(480, 160)
        coin7 = Coin(2440, 160)
        coin8 = Coin(400, 240)
        coin9 = Coin(320, 320)
        coin10 = Coin(4280, 320)
        coin11 = Coin(3600, 360)
        coin12 = Coin(560, 400)
        coin13 = Coin(2200, 400)
        coin14 = Coin(3760, 400)
        coin15 = Coin(1120, 480)
        coin16 = Coin(320, 520)
        coin17 = Coin(840, 520)
        coin18 = Coin(2120, 520)
        coin19 = Coin(3960, 520)
        self.coins = pygame.sprite.Group(coin0, coin1, coin2, coin3,
                                         coin4, coin5, coin6, coin7,
                                         coin8, coin9, coin10, coin11,
                                         coin12, coin13, coin14, coin15,
                                         coin16, coin17, coin18, coin19)

    def set_blocks(self):
        """Создает все блоки для уровня"""
        block0 = Block(2040, 120, 'city')
        block1 = Block(2080, 120, 'city')
        block2 = Block(2120, 120, 'city')
        block3 = Block(3000, 120, 'city')
        block4 = Block(3040, 120, 'city')
        block5 = Block(3080, 120, 'city')
        block6 = Block(3120, 120, 'city')
        block7 = Block(2960, 160, 'city')
        block8 = Block(3000, 160, 'city')
        block9 = Block(3040, 160, 'city')
        block10 = Block(3080, 160, 'city')
        block11 = Block(3120, 160, 'city')
        block12 = Block(3160, 160, 'city')
        block13 = Block(640, 200, 'city')
        block14 = Block(1960, 200, 'city')
        block15 = Block(2400, 200, 'city')
        block16 = Block(2440, 200, 'city')
        block17 = Block(2480, 200, 'city')
        block18 = Block(600, 240, 'city')
        block19 = Block(640, 240, 'city')
        block20 = Block(680, 240, 'city')
        block21 = Block(1960, 240, 'city')
        block22 = Block(2680, 240, 'city')
        block23 = Block(2720, 240, 'city')
        block24 = Block(2880, 240, 'city')
        block25 = Block(520, 280, 'city')
        block26 = Block(560, 280, 'city')
        block27 = Block(600, 280, 'city')
        block28 = Block(640, 280, 'city')
        block29 = Block(680, 280, 'city')
        block30 = Block(1880, 280, 'city')
        block31 = Block(1960, 280, 'city')
        block32 = Block(2320, 280, 'city')
        block33 = Block(2880, 280, 'city')
        block34 = Block(520, 320, 'city')
        block35 = Block(560, 320, 'city')
        block36 = Block(600, 320, 'city')
        block37 = Block(640, 320, 'city')
        block38 = Block(680, 320, 'city')
        block39 = Block(1880, 320, 'city')
        block40 = Block(1960, 320, 'city')
        block41 = Block(2800, 320, 'city')
        block42 = Block(2880, 320, 'city')
        block43 = Block(440, 360, 'city')
        block44 = Block(520, 360, 'city')
        block45 = Block(560, 360, 'city')
        block46 = Block(600, 360, 'city')
        block47 = Block(680, 360, 'city')
        block48 = Block(1800, 360, 'city')
        block49 = Block(1880, 360, 'city')
        block50 = Block(1960, 360, 'city')
        block51 = Block(2240, 360, 'city')
        block52 = Block(2800, 360, 'city')
        block53 = Block(2880, 360, 'city')
        block54 = Block(440, 400, 'city')
        block55 = Block(520, 400, 'city')
        block56 = Block(600, 400, 'city')
        block57 = Block(880, 400, 'city')
        block58 = Block(1800, 400, 'city')
        block59 = Block(1880, 400, 'city')
        block60 = Block(1960, 400, 'city')
        block61 = Block(2240, 400, 'city')
        block62 = Block(2400, 400, 'city')
        block63 = Block(2440, 400, 'city')
        block64 = Block(2480, 400, 'city')
        block65 = Block(2720, 400, 'city')
        block66 = Block(2800, 400, 'city')
        block67 = Block(2880, 400, 'city')
        block68 = Block(360, 440, 'city')
        block69 = Block(440, 440, 'city')
        block70 = Block(480, 440, 'city')
        block71 = Block(520, 440, 'city')
        block72 = Block(880, 440, 'city')
        block73 = Block(1720, 440, 'city')
        block74 = Block(1800, 440, 'city')
        block75 = Block(1880, 440, 'city')
        block76 = Block(1960, 440, 'city')
        block77 = Block(2160, 440, 'city')
        block78 = Block(2240, 440, 'city')
        block79 = Block(2720, 440, 'city')
        block80 = Block(2800, 440, 'city')
        block81 = Block(2880, 440, 'city')
        block82 = Block(3160, 440, 'city')
        block83 = Block(3680, 440, 'city')
        block84 = Block(3920, 440, 'city')
        block85 = Block(4320, 440, 'city')
        block86 = Block(360, 480, 'city')
        block87 = Block(440, 480, 'city')
        block88 = Block(480, 480, 'city')
        block89 = Block(520, 480, 'city')
        block90 = Block(800, 480, 'city')
        block91 = Block(880, 480, 'city')
        block92 = Block(1160, 480, 'city')
        block93 = Block(1360, 480, 'city')
        block94 = Block(1960, 480, 'city')
        block95 = Block(2160, 480, 'city')
        block96 = Block(2640, 480, 'city')
        block97 = Block(2880, 480, 'city')
        block98 = Block(3160, 480, 'city')
        block99 = Block(3680, 480, 'city')
        block100 = Block(3920, 480, 'city')
        block101 = Block(4320, 480, 'city')
        block102 = Block(280, 520, 'city')
        block103 = Block(360, 520, 'city')
        block104 = Block(400, 520, 'city')
        block105 = Block(440, 520, 'city')
        block106 = Block(480, 520, 'city')
        block107 = Block(520, 520, 'city')
        block108 = Block(800, 520, 'city')
        block109 = Block(880, 520, 'city')
        block110 = Block(920, 520, 'city')
        block111 = Block(960, 520, 'city')
        block112 = Block(1000, 520, 'city')
        block113 = Block(1040, 520, 'city')
        block114 = Block(1080, 520, 'city')
        block115 = Block(1120, 520, 'city')
        block116 = Block(1160, 520, 'city')
        block117 = Block(1200, 520, 'city')
        block118 = Block(1240, 520, 'city')
        block119 = Block(1280, 520, 'city')
        block120 = Block(1320, 520, 'city')
        block121 = Block(1360, 520, 'city')
        block122 = Block(1640, 520, 'city')
        block123 = Block(1960, 520, 'city')
        block124 = Block(2080, 520, 'city')
        block125 = Block(2160, 520, 'city')
        block126 = Block(2880, 520, 'city')
        block127 = Block(3080, 520, 'city')
        block128 = Block(3160, 520, 'city')
        block129 = Block(3600, 520, 'city')
        block130 = Block(3680, 520, 'city')
        block131 = Block(3840, 520, 'city')
        block132 = Block(3920, 520, 'city')
        block133 = Block(4240, 520, 'city')
        block134 = Block(4320, 520, 'city')
        block135 = Block(0, 560, 'city')
        block136 = Block(40, 560, 'city')
        block137 = Block(80, 560, 'city')
        block138 = Block(120, 560, 'city')
        block139 = Block(160, 560, 'city')
        block140 = Block(200, 560, 'city')
        block141 = Block(240, 560, 'city')
        block142 = Block(280, 560, 'city')
        block143 = Block(320, 560, 'city')
        block144 = Block(360, 560, 'city')
        block145 = Block(400, 560, 'city')
        block146 = Block(440, 560, 'city')
        block147 = Block(480, 560, 'city')
        block148 = Block(520, 560, 'city')
        block149 = Block(560, 560, 'city')
        block150 = Block(600, 560, 'city')
        block151 = Block(640, 560, 'city')
        block152 = Block(680, 560, 'city')
        block153 = Block(720, 560, 'city')
        block154 = Block(760, 560, 'city')
        block155 = Block(800, 560, 'city')
        block156 = Block(840, 560, 'city')
        block157 = Block(880, 560, 'city')
        block158 = Block(920, 560, 'city')
        block159 = Block(960, 560, 'city')
        block160 = Block(1000, 560, 'city')
        block161 = Block(1040, 560, 'city')
        block162 = Block(1080, 560, 'city')
        block163 = Block(1120, 560, 'city')
        block164 = Block(1160, 560, 'city')
        block165 = Block(1200, 560, 'city')
        block166 = Block(1240, 560, 'city')
        block167 = Block(1280, 560, 'city')
        block168 = Block(1320, 560, 'city')
        block169 = Block(1360, 560, 'city')
        block170 = Block(1400, 560, 'city')
        block171 = Block(1440, 560, 'city')
        block172 = Block(1480, 560, 'city')
        block173 = Block(1520, 560, 'city')
        block174 = Block(1560, 560, 'city')
        block175 = Block(1600, 560, 'city')
        block176 = Block(1640, 560, 'city')
        block177 = Block(1680, 560, 'city')
        block178 = Block(1720, 560, 'city')
        block179 = Block(1760, 560, 'city')
        block180 = Block(1800, 560, 'city')
        block181 = Block(1840, 560, 'city')
        block182 = Block(1880, 560, 'city')
        block183 = Block(1920, 560, 'city')
        block184 = Block(1960, 560, 'city')
        block185 = Block(2000, 560, 'city')
        block186 = Block(2040, 560, 'city')
        block187 = Block(2080, 560, 'city')
        block188 = Block(2120, 560, 'city')
        block189 = Block(2160, 560, 'city')
        block190 = Block(2200, 560, 'city')
        block191 = Block(2240, 560, 'city')
        block192 = Block(2280, 560, 'city')
        block193 = Block(2320, 560, 'city')
        block194 = Block(2360, 560, 'city')
        block195 = Block(2400, 560, 'city')
        block196 = Block(2440, 560, 'city')
        block197 = Block(2480, 560, 'city')
        block198 = Block(2520, 560, 'city')
        block199 = Block(2560, 560, 'city')
        block200 = Block(2600, 560, 'city')
        block201 = Block(2640, 560, 'city')
        block202 = Block(2680, 560, 'city')
        block203 = Block(2720, 560, 'city')
        block204 = Block(2760, 560, 'city')
        block205 = Block(2800, 560, 'city')
        block206 = Block(2840, 560, 'city')
        block207 = Block(2880, 560, 'city')
        block208 = Block(2920, 560, 'city')
        block209 = Block(2960, 560, 'city')
        block210 = Block(3000, 560, 'city')
        block211 = Block(3040, 560, 'city')
        block212 = Block(3080, 560, 'city')
        block213 = Block(3120, 560, 'city')
        block214 = Block(3160, 560, 'city')
        block215 = Block(3200, 560, 'city')
        block216 = Block(3240, 560, 'city')
        block217 = Block(3280, 560, 'city')
        block218 = Block(3320, 560, 'city')
        block219 = Block(3360, 560, 'city')
        block220 = Block(3400, 560, 'city')
        block221 = Block(3440, 560, 'city')
        block222 = Block(3480, 560, 'city')
        block223 = Block(3520, 560, 'city')
        block224 = Block(3560, 560, 'city')
        block225 = Block(3600, 560, 'city')
        block226 = Block(3640, 560, 'city')
        block227 = Block(3680, 560, 'city')
        block228 = Block(3720, 560, 'city')
        block229 = Block(3760, 560, 'city')
        block230 = Block(3800, 560, 'city')
        block231 = Block(3840, 560, 'city')
        block232 = Block(3880, 560, 'city')
        block233 = Block(3920, 560, 'city')
        block234 = Block(3960, 560, 'city')
        block235 = Block(4000, 560, 'city')
        block236 = Block(4040, 560, 'city')
        block237 = Block(4080, 560, 'city')
        block238 = Block(4120, 560, 'city')
        block239 = Block(4160, 560, 'city')
        block240 = Block(4200, 560, 'city')
        block241 = Block(4240, 560, 'city')
        block242 = Block(4280, 560, 'city')
        block243 = Block(4320, 560, 'city')
        block244 = Block(4360, 560, 'city')
        block245 = Block(4400, 560, 'city')
        block246 = Block(4440, 560, 'city')
        block247 = Block(4480, 560, 'city')
        block248 = Block(4520, 560, 'city')
        block249 = Block(4560, 560, 'city')
        block250 = Block(4600, 560, 'city')
        block251 = Block(4640, 560, 'city')
        block252 = Block(4680, 560, 'city')
        block253 = Block(4720, 560, 'city')
        block254 = Block(4760, 560, 'city')
        block255 = Block(4800, 560, 'city')
        block256 = Block(4840, 560, 'city')
        block257 = Block(4880, 560, 'city')
        block258 = Block(4920, 560, 'city')
        block259 = Block(4960, 560, 'city')

        self.blocks = pygame.sprite.Group(block0, block1,
                                          block2, block3,
                                          block4, block5,
                                          block6, block7,
                                          block8, block9,
                                          block10, block11,
                                          block12, block13,
                                          block14, block15,
                                          block16, block17,
                                          block18, block19,
                                          block20, block21,
                                          block22, block23,
                                          block24, block25,
                                          block26, block27,
                                          block28, block29,
                                          block30, block31,
                                          block32, block33,
                                          block34, block35,
                                          block36, block37,
                                          block38, block39,
                                          block40, block41,
                                          block42, block43,
                                          block44, block45,
                                          block46, block47,
                                          block48, block49,
                                          block50, block51,
                                          block52, block53,
                                          block54, block55,
                                          block56, block57,
                                          block58, block59,
                                          block60, block61,
                                          block62, block63,
                                          block64, block65,
                                          block66, block67,
                                          block68, block69,
                                          block70, block71,
                                          block72, block73,
                                          block74, block75,
                                          block76, block77,
                                          block78, block79,
                                          block80, block81,
                                          block82, block83,
                                          block84, block85,
                                          block86, block87,
                                          block88, block89,
                                          block90, block91,
                                          block92, block93,
                                          block94, block95,
                                          block96, block97,
                                          block98, block99,
                                          block100, block101,
                                          block102, block103,
                                          block104, block105,
                                          block106, block107,
                                          block108, block109,
                                          block110, block111,
                                          block112, block113,
                                          block114, block115,
                                          block116, block117,
                                          block118, block119,
                                          block120, block121,
                                          block122, block123,
                                          block124, block125,
                                          block126, block127,
                                          block128, block129,
                                          block130, block131,
                                          block132, block133,
                                          block134, block135,
                                          block136, block137,
                                          block138, block139,
                                          block140, block141,
                                          block142, block143,
                                          block144, block145,
                                          block146, block147,
                                          block148, block149,
                                          block150, block151,
                                          block152, block153,
                                          block154, block155,
                                          block156, block157,
                                          block158, block159,
                                          block160, block161,
                                          block162, block163,
                                          block164, block165,
                                          block166, block167,
                                          block168, block169,
                                          block170, block171,
                                          block172, block173,
                                          block174, block175,
                                          block176, block177,
                                          block178, block179,
                                          block180, block181,
                                          block182, block183,
                                          block184, block185,
                                          block186, block187,
                                          block188, block189,
                                          block190, block191,
                                          block192, block193,
                                          block194, block195,
                                          block196, block197,
                                          block198, block199,
                                          block200, block201,
                                          block202, block203,
                                          block204, block205,
                                          block206, block207,
                                          block208, block209,
                                          block210, block211,
                                          block212, block213,
                                          block214, block215,
                                          block216, block217,
                                          block218, block219,
                                          block220, block221,
                                          block222, block223,
                                          block224, block225,
                                          block226, block227,
                                          block228, block229,
                                          block230, block231,
                                          block232, block233,
                                          block234, block235,
                                          block236, block237,
                                          block238, block239,
                                          block240, block241,
                                          block242, block243,
                                          block244, block245,
                                          block246, block247,
                                          block248, block249,
                                          block250, block251,
                                          block252, block253,
                                          block254, block255,
                                          block256, block257,
                                          block258, block259)

    def set_enemies(self):
        """Создание врагов для уровня"""
        cop0 = enemies.Cop(2120, 120)
        cop_group0 = pygame.sprite.Group(cop0)
        cop1 = enemies.Cop(3160, 160)
        cop_group1 = pygame.sprite.Group(cop1)
        cop2 = enemies.Cop(1040, 520)
        cop_group2 = pygame.sprite.Group(cop2)
        cop3 = enemies.Cop(600, 560)
        cop_group3 = pygame.sprite.Group(cop3)
        cop4 = enemies.Cop(1560, 560)
        cop_group4 = pygame.sprite.Group(cop4)
        cop5 = enemies.Cop(2560, 560)
        cop_group5 = pygame.sprite.Group(cop5)
        cop6 = enemies.Cop(3440, 560)
        cop_group6 = pygame.sprite.Group(cop6)
        cop7 = enemies.Cop(3760, 560)
        cop_group7 = pygame.sprite.Group(cop7)
        granny0 = enemies.Granny(2480, 400)
        granny_group0 = pygame.sprite.Group(granny0)
        granny1 = enemies.Granny(1320, 520)
        granny_group1 = pygame.sprite.Group(granny1)
        granny2 = enemies.Granny(1880, 560)
        granny_group2 = pygame.sprite.Group(granny2)
        granny3 = enemies.Granny(4120, 560)
        granny_group3 = pygame.sprite.Group(granny3)
        self.enemies = [cop0, cop1, cop2, cop3, cop4,
                        cop5, cop6, cop7, granny0,
                        granny1, granny2, granny3]
        self.enemy_group_list = [cop_group0, cop_group1, cop_group2,
                                 cop_group3, cop_group4, cop_group5,
                                 cop_group6, cop_group7,
                                 granny_group0, granny_group1,
                                 granny_group2, granny_group3]

    def set_checkpoints(self):
        """Создание чекпоинтов"""
        check1 = checkpoint.Checkpoint(1120, "1")
        check2 = checkpoint.Checkpoint(2160, '2')
        check3 = checkpoint.Checkpoint(110, '3')
        check4 = checkpoint.Checkpoint(110, "4")
        check5 = checkpoint.Checkpoint(560, '5')
        check6 = checkpoint.Checkpoint(1560, '6')
        check7 = checkpoint.Checkpoint(2440, '7')
        check8 = checkpoint.Checkpoint(2760, "8")
        check9 = checkpoint.Checkpoint(1480, '9')
        check10 = checkpoint.Checkpoint(320, '10')
        check11 = checkpoint.Checkpoint(880, "11")
        check12 = checkpoint.Checkpoint(3120, '12')
        self.check_point_group = pygame.sprite.Group(check1, check2,
                                                     check3, check4,
                                                     check5, check6,
                                                     check7, check8,
                                                     check9, check10,
                                                     check11,
                                                     check12)

    def set_spritegroups(self):
        """Создает группу спрайтов"""
        self.enemy_group = pygame.sprite.Group()
        self.hero_and_enemy_group = pygame.sprite.Group(self.hero,
                                                        self.enemy_group)

    def on_update(self, keys):
        """ Обновляет весь уровень, используя состояния.
            Вызывается объектом управления"""
        self.update_everything(keys)
        self.blit_everything()
        self.update_viewport()

    def update_everything(self, keys):
        """Обновляет местоположение всех спрайтов на экране"""
        self.hero.update(keys, {})
        self.info_coin.rect.x = self.viewport.x + 1000 - self.info_coin.w
        self.info_hearts.rect.x = self.viewport.x
        self.check_cp()
        self.info.update()
        for i in self.enemies:
            i.update(keys)
        self.sprite_positions()
        self.coins.update()
        self.end_of_level()

    def end_of_level(self):
        """Конец уровня"""
        if self.hero.rect.x >= 4900:
            self.done = True

    def sprite_positions(self):
        """Регулирует спрайты по их скоростям x и y и столкновению"""
        self.hero_position()
        self.enemy_position()

    def hero_position(self):
        """Регулирует положение героя на основе его скоростей x, y и
         потенциальные столкновения"""
        self.last_x_position = self.hero.rect.right
        self.hero.rect.x += round(self.hero.x_vel)
        self.x_collisions_hero()

        self.hero.rect.y += round(self.hero.y_vel)
        self.y_collisions_hero()

        if self.hero.rect.x < (self.viewport.x + 5):
            self.hero.rect.x = (self.viewport.x + 5)

    def x_collisions_hero(self):
        """Проверяет наличие столкновений, когда герой движется вдоль оси X"""
        bricks = pygame.sprite.spritecollideany(self.hero, self.blocks)
        enemy = pygame.sprite.spritecollideany(self.hero, self.enemy_group)
        coin = pygame.sprite.spritecollideany(self.hero, self.coins)
        bottle = pygame.sprite.spritecollideany(self.hero, self.healing)

        if bricks:
            self.x_collisions_solve(bricks)

        elif enemy:
            if self.hero.flag:
                enemy.kill()
            else:
                self.info_hearts.number -= 1
                if self.info_hearts.number == 0:
                    self.next_state = "LOOSE_GAME"
                    self.done = True
                self.x_collisions_solve(enemy)

        elif coin:
            self.info_coin.number += 1
            coin.kill()

        elif bottle:
            if self.info_hearts.number < 3:
                self.info_hearts.number += 1
            bottle.kill()

    def x_collisions_solve(self, collider):
        """Разрешает колизии по оси X"""
        self.hero.x_vel = 0
        if self.hero.rect.x < collider.rect.x:
            self.hero.rect.right = collider.rect.left
        else:
            self.hero.rect.left = collider.rect.right

    def y_collisions_hero(self):
        """Проверяет наличие столкновений, когда герой движется вдоль оси Y"""
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
        """Проверяет наличие столкновений, когда враг движется вдоль оси X"""
        bricks = pygame.sprite.spritecollideany(i, self.blocks)
        enemy = pygame.sprite.spritecollideany(self.hero, self.enemy_group)

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
        """Прорисовывает все спрайты на основную поверхность"""
        pygame.display.flip()
        self.level.blit(self.background, self.viewport, self.viewport)
        self.coins.draw(self.level)
        self.info.draw(self.level)
        self.blocks.draw(self.level)
        self.healing.draw(self.level)
        self.hero_and_enemy_group.draw(self.level)
        screen.blit(self.level, (0,0), self.viewport)        

    def check_cp(self):
        '''Определяет, если происходит столкновение контрольной точки,
           удаляет контрольную точку,
           добавляет врагов в self.enemy_group'''
        checkpoint = pygame.sprite.spritecollideany(self.hero,
                                                    self.check_point_group)
        if checkpoint:
            checkpoint.kill()
            for i in range(1, 15):
                if checkpoint.name == str(i):
                    self.enemy_group.add(self.enemy_group_list[i-1])
            self.hero_and_enemy_group.add(self.enemy_group)

    def get_event(self, event):
        """Создает кнопку - слудующий уровень"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 900 and\
               pygame.mouse.get_pos()[1] >= 50:
                if pygame.mouse.get_pos()[0] <= 950 and \
                   pygame.mouse.get_pos()[1] <= 100:
                    self.done = True

    def update_viewport(self):
        """Меняет вид камеры"""
        if (self.viewport.x <= 4000):
            third = self.viewport.x + self.viewport.w//3
            play_center = self.hero.rect.centerx
            play_right = self.hero.rect.right

            if self.hero.x_vel > 0 and play_center >= third:
                mult = 1 if play_right < self.viewport.centerx else 2
                new = self.viewport.x + mult * self.hero.x_vel
                highest = self.level_rect.w - self.viewport.w
                self.viewport.x = min(highest, new)
