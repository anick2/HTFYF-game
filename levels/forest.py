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
        
        block0 = Block(4560, 80)
        block1 = Block(2840, 160)
        block2 = Block(2880, 160)
        block3 = Block(2920, 160)
        block4 = Block(2960, 160)
        block5 = Block(3000, 160)
        block6 = Block(3040, 160)
        block7 = Block(3080, 160)
        block8 = Block(3400, 160)
        block9 = Block(520, 200)
        block10 = Block(960, 200)
        block11 = Block(3120, 200)
        block12 = Block(3160, 200)
        block13 = Block(3200, 200)
        block14 = Block(3360, 200)
        block15 = Block(3400, 200)
        block16 = Block(3440, 200)
        block17 = Block(3480, 200)
        block18 = Block(3520, 200)
        block19 = Block(3560, 200)
        block20 = Block(3600, 200)
        block21 = Block(3640, 200)
        block22 = Block(3680, 200)
        block23 = Block(3720, 200)
        block24 = Block(3760, 200)
        block25 = Block(3800, 200)
        block26 = Block(3840, 200)
        block27 = Block(3880, 200)
        block28 = Block(3920, 200)
        block29 = Block(3960, 200)
        block30 = Block(4000, 200)
        block31 = Block(4040, 200)
        block32 = Block(4080, 200)
        block33 = Block(4120, 200)
        block34 = Block(4160, 200)
        block35 = Block(4200, 200)
        block36 = Block(4240, 200)
        block37 = Block(4280, 200)
        block38 = Block(4520, 200)
        block39 = Block(3320, 240)
        block40 = Block(3360, 240)
        block41 = Block(3400, 240)
        block42 = Block(3440, 240)
        block43 = Block(3480, 240)
        block44 = Block(3520, 240)
        block45 = Block(3560, 240)
        block46 = Block(3600, 240)
        block47 = Block(3640, 240)
        block48 = Block(3680, 240)
        block49 = Block(3720, 240)
        block50 = Block(3760, 240)
        block51 = Block(3800, 240)
        block52 = Block(3840, 240)
        block53 = Block(3880, 240)
        block54 = Block(3920, 240)
        block55 = Block(3960, 240)
        block56 = Block(4000, 240)
        block57 = Block(4040, 240)
        block58 = Block(4080, 240)
        block59 = Block(4120, 240)
        block60 = Block(4160, 240)
        block61 = Block(4200, 240)
        block62 = Block(4240, 240)
        block63 = Block(4280, 240)
        block64 = Block(3280, 280)
        block65 = Block(3320, 280)
        block66 = Block(3360, 280)
        block67 = Block(3400, 280)
        block68 = Block(3440, 280)
        block69 = Block(3480, 280)
        block70 = Block(3520, 280)
        block71 = Block(3560, 280)
        block72 = Block(3600, 280)
        block73 = Block(3640, 280)
        block74 = Block(3680, 280)
        block75 = Block(3720, 280)
        block76 = Block(3760, 280)
        block77 = Block(3800, 280)
        block78 = Block(3840, 280)
        block79 = Block(3880, 280)
        block80 = Block(3920, 280)
        block81 = Block(3960, 280)
        block82 = Block(4000, 280)
        block83 = Block(4040, 280)
        block84 = Block(4080, 280)
        block85 = Block(4120, 280)
        block86 = Block(4160, 280)
        block87 = Block(4200, 280)
        block88 = Block(4240, 280)
        block89 = Block(4280, 280)
        block90 = Block(480, 320)
        block91 = Block(880, 320)
        block92 = Block(920, 320)
        block93 = Block(960, 320)
        block94 = Block(3240, 320)
        block95 = Block(3280, 320)
        block96 = Block(3320, 320)
        block97 = Block(3360, 320)
        block98 = Block(3400, 320)
        block99 = Block(3440, 320)
        block100 = Block(3480, 320)
        block101 = Block(3520, 320)
        block102 = Block(3560, 320)
        block103 = Block(3600, 320)
        block104 = Block(3640, 320)
        block105 = Block(3680, 320)
        block106 = Block(3720, 320)
        block107 = Block(3760, 320)
        block108 = Block(3800, 320)
        block109 = Block(3840, 320)
        block110 = Block(3880, 320)
        block111 = Block(3920, 320)
        block112 = Block(3960, 320)
        block113 = Block(4000, 320)
        block114 = Block(4040, 320)
        block115 = Block(4080, 320)
        block116 = Block(4120, 320)
        block117 = Block(4160, 320)
        block118 = Block(4200, 320)
        block119 = Block(4240, 320)
        block120 = Block(4280, 320)
        block121 = Block(4320, 320)
        block122 = Block(4360, 320)
        block123 = Block(4400, 320)
        block124 = Block(4440, 320)
        block125 = Block(4480, 320)
        block126 = Block(4520, 320)
        block127 = Block(4560, 320)
        block128 = Block(2600, 360)
        block129 = Block(2640, 360)
        block130 = Block(2680, 360)
        block131 = Block(2720, 360)
        block132 = Block(2760, 360)
        block133 = Block(2800, 360)
        block134 = Block(2840, 360)
        block135 = Block(3200, 360)
        block136 = Block(3240, 360)
        block137 = Block(3280, 360)
        block138 = Block(3320, 360)
        block139 = Block(3360, 360)
        block140 = Block(3400, 360)
        block141 = Block(3440, 360)
        block142 = Block(3480, 360)
        block143 = Block(3520, 360)
        block144 = Block(3560, 360)
        block145 = Block(3600, 360)
        block146 = Block(3640, 360)
        block147 = Block(3680, 360)
        block148 = Block(3720, 360)
        block149 = Block(3760, 360)
        block150 = Block(3800, 360)
        block151 = Block(3840, 360)
        block152 = Block(3880, 360)
        block153 = Block(3920, 360)
        block154 = Block(3960, 360)
        block155 = Block(4000, 360)
        block156 = Block(4040, 360)
        block157 = Block(4080, 360)
        block158 = Block(4120, 360)
        block159 = Block(4160, 360)
        block160 = Block(4200, 360)
        block161 = Block(4240, 360)
        block162 = Block(4280, 360)
        block163 = Block(4320, 360)
        block164 = Block(4360, 360)
        block165 = Block(4400, 360)
        block166 = Block(4440, 360)
        block167 = Block(4480, 360)
        block168 = Block(4520, 360)
        block169 = Block(4560, 360)
        block170 = Block(2400, 400)
        block171 = Block(2440, 400)
        block172 = Block(2480, 400)
        block173 = Block(2520, 400)
        block174 = Block(2560, 400)
        block175 = Block(2600, 400)
        block176 = Block(2800, 400)
        block177 = Block(2840, 400)
        block178 = Block(3160, 400)
        block179 = Block(3200, 400)
        block180 = Block(3240, 400)
        block181 = Block(3280, 400)
        block182 = Block(3320, 400)
        block183 = Block(3360, 400)
        block184 = Block(3400, 400)
        block185 = Block(3440, 400)
        block186 = Block(3480, 400)
        block187 = Block(3520, 400)
        block188 = Block(3560, 400)
        block189 = Block(3600, 400)
        block190 = Block(3640, 400)
        block191 = Block(3680, 400)
        block192 = Block(3720, 400)
        block193 = Block(3760, 400)
        block194 = Block(3800, 400)
        block195 = Block(3840, 400)
        block196 = Block(3880, 400)
        block197 = Block(3920, 400)
        block198 = Block(3960, 400)
        block199 = Block(4000, 400)
        block200 = Block(4040, 400)
        block201 = Block(4080, 400)
        block202 = Block(4120, 400)
        block203 = Block(4160, 400)
        block204 = Block(4200, 400)
        block205 = Block(4240, 400)
        block206 = Block(4280, 400)
        block207 = Block(4320, 400)
        block208 = Block(4360, 400)
        block209 = Block(4400, 400)
        block210 = Block(4440, 400)
        block211 = Block(4480, 400)
        block212 = Block(4520, 400)
        block213 = Block(4560, 400)
        block214 = Block(440, 440)
        block215 = Block(520, 440)
        block216 = Block(560, 440)
        block217 = Block(840, 440)
        block218 = Block(880, 440)
        block219 = Block(1400, 440)
        block220 = Block(1440, 440)
        block221 = Block(1480, 440)
        block222 = Block(2280, 440)
        block223 = Block(2320, 440)
        block224 = Block(2360, 440)
        block225 = Block(2400, 440)
        block226 = Block(2440, 440)
        block227 = Block(2480, 440)
        block228 = Block(2520, 440)
        block229 = Block(2560, 440)
        block230 = Block(2600, 440)
        block231 = Block(3120, 440)
        block232 = Block(3160, 440)
        block233 = Block(3200, 440)
        block234 = Block(3240, 440)
        block235 = Block(3280, 440)
        block236 = Block(3320, 440)
        block237 = Block(3360, 440)
        block238 = Block(3400, 440)
        block239 = Block(3440, 440)
        block240 = Block(3480, 440)
        block241 = Block(3520, 440)
        block242 = Block(3560, 440)
        block243 = Block(3600, 440)
        block244 = Block(3640, 440)
        block245 = Block(3680, 440)
        block246 = Block(3720, 440)
        block247 = Block(3760, 440)
        block248 = Block(3800, 440)
        block249 = Block(3840, 440)
        block250 = Block(3880, 440)
        block251 = Block(3920, 440)
        block252 = Block(3960, 440)
        block253 = Block(4000, 440)
        block254 = Block(4040, 440)
        block255 = Block(4080, 440)
        block256 = Block(4120, 440)
        block257 = Block(4160, 440)
        block258 = Block(4200, 440)
        block259 = Block(4240, 440)
        block260 = Block(4280, 440)
        block261 = Block(4320, 440)
        block262 = Block(4360, 440)
        block263 = Block(4400, 440)
        block264 = Block(4440, 440)
        block265 = Block(4480, 440)
        block266 = Block(4520, 440)
        block267 = Block(4560, 440)
        block268 = Block(4600, 440)
        block269 = Block(4640, 440)
        block270 = Block(4680, 440)
        block271 = Block(400, 480)
        block272 = Block(440, 480)
        block273 = Block(520, 480)
        block274 = Block(560, 480)
        block275 = Block(600, 480)
        block276 = Block(640, 480)
        block277 = Block(800, 480)
        block278 = Block(840, 480)
        block279 = Block(880, 480)
        block280 = Block(920, 480)
        block281 = Block(1120, 480)
        block282 = Block(1400, 480)
        block283 = Block(1440, 480)
        block284 = Block(1480, 480)
        block285 = Block(1520, 480)
        block286 = Block(1560, 480)
        block287 = Block(1600, 480)
        block288 = Block(1760, 480)
        block289 = Block(2280, 480)
        block290 = Block(2320, 480)
        block291 = Block(2360, 480)
        block292 = Block(2400, 480)
        block293 = Block(2440, 480)
        block294 = Block(2480, 480)
        block295 = Block(2520, 480)
        block296 = Block(2560, 480)
        block297 = Block(2600, 480)
        block298 = Block(3080, 480)
        block299 = Block(3120, 480)
        block300 = Block(3160, 480)
        block301 = Block(3200, 480)
        block302 = Block(3240, 480)
        block303 = Block(3280, 480)
        block304 = Block(3320, 480)
        block305 = Block(3360, 480)
        block306 = Block(3400, 480)
        block307 = Block(3440, 480)
        block308 = Block(3480, 480)
        block309 = Block(3520, 480)
        block310 = Block(3560, 480)
        block311 = Block(3600, 480)
        block312 = Block(3640, 480)
        block313 = Block(3680, 480)
        block314 = Block(3720, 480)
        block315 = Block(3760, 480)
        block316 = Block(3800, 480)
        block317 = Block(3840, 480)
        block318 = Block(3880, 480)
        block319 = Block(3920, 480)
        block320 = Block(3960, 480)
        block321 = Block(4000, 480)
        block322 = Block(4040, 480)
        block323 = Block(4080, 480)
        block324 = Block(4120, 480)
        block325 = Block(4160, 480)
        block326 = Block(4200, 480)
        block327 = Block(4240, 480)
        block328 = Block(4280, 480)
        block329 = Block(4320, 480)
        block330 = Block(4360, 480)
        block331 = Block(4400, 480)
        block332 = Block(4440, 480)
        block333 = Block(4480, 480)
        block334 = Block(4520, 480)
        block335 = Block(4560, 480)
        block336 = Block(4600, 480)
        block337 = Block(4640, 480)
        block338 = Block(4680, 480)
        block339 = Block(360, 520)
        block340 = Block(400, 520)
        block341 = Block(440, 520)
        block342 = Block(520, 520)
        block343 = Block(560, 520)
        block344 = Block(600, 520)
        block345 = Block(640, 520)
        block346 = Block(760, 520)
        block347 = Block(800, 520)
        block348 = Block(840, 520)
        block349 = Block(880, 520)
        block350 = Block(920, 520)
        block351 = Block(960, 520)
        block352 = Block(1080, 520)
        block353 = Block(1120, 520)
        block354 = Block(1400, 520)
        block355 = Block(1440, 520)
        block356 = Block(1480, 520)
        block357 = Block(1520, 520)
        block358 = Block(1560, 520)
        block359 = Block(1600, 520)
        block360 = Block(1720, 520)
        block361 = Block(1760, 520)
        block362 = Block(1800, 520)
        block363 = Block(2120, 520)
        block364 = Block(2160, 520)
        block365 = Block(2200, 520)
        block366 = Block(2240, 520)
        block367 = Block(2280, 520)
        block368 = Block(2320, 520)
        block369 = Block(2360, 520)
        block370 = Block(2400, 520)
        block371 = Block(2440, 520)
        block372 = Block(2480, 520)
        block373 = Block(2520, 520)
        block374 = Block(2560, 520)
        block375 = Block(2600, 520)
        block376 = Block(3040, 520)
        block377 = Block(3080, 520)
        block378 = Block(3120, 520)
        block379 = Block(3160, 520)
        block380 = Block(3200, 520)
        block381 = Block(3240, 520)
        block382 = Block(3280, 520)
        block383 = Block(3320, 520)
        block384 = Block(3360, 520)
        block385 = Block(3400, 520)
        block386 = Block(3440, 520)
        block387 = Block(3480, 520)
        block388 = Block(3520, 520)
        block389 = Block(3560, 520)
        block390 = Block(3600, 520)
        block391 = Block(3640, 520)
        block392 = Block(3680, 520)
        block393 = Block(3720, 520)
        block394 = Block(3760, 520)
        block395 = Block(3800, 520)
        block396 = Block(3840, 520)
        block397 = Block(3880, 520)
        block398 = Block(3920, 520)
        block399 = Block(3960, 520)
        block400 = Block(4000, 520)
        block401 = Block(4040, 520)
        block402 = Block(4080, 520)
        block403 = Block(4120, 520)
        block404 = Block(4160, 520)
        block405 = Block(4200, 520)
        block406 = Block(4240, 520)
        block407 = Block(4280, 520)
        block408 = Block(4320, 520)
        block409 = Block(4360, 520)
        block410 = Block(4400, 520)
        block411 = Block(4440, 520)
        block412 = Block(4480, 520)
        block413 = Block(4520, 520)
        block414 = Block(4560, 520)
        block415 = Block(4600, 520)
        block416 = Block(4640, 520)
        block417 = Block(4680, 520)
        block418 = Block(0, 560)
        block419 = Block(40, 560)
        block420 = Block(80, 560)
        block421 = Block(120, 560)
        block422 = Block(160, 560)
        block423 = Block(200, 560)
        block424 = Block(240, 560)
        block425 = Block(280, 560)
        block426 = Block(320, 560)
        block427 = Block(360, 560)
        block428 = Block(400, 560)
        block429 = Block(440, 560)
        block430 = Block(480, 560)
        block431 = Block(520, 560)
        block432 = Block(560, 560)
        block433 = Block(600, 560)
        block434 = Block(640, 560)
        block435 = Block(680, 560)
        block436 = Block(720, 560)
        block437 = Block(760, 560)
        block438 = Block(800, 560)
        block439 = Block(840, 560)
        block440 = Block(880, 560)
        block441 = Block(920, 560)
        block442 = Block(960, 560)
        block443 = Block(1000, 560)
        block444 = Block(1040, 560)
        block445 = Block(1080, 560)
        block446 = Block(1120, 560)
        block447 = Block(1160, 560)
        block448 = Block(1200, 560)
        block449 = Block(1240, 560)
        block450 = Block(1280, 560)
        block451 = Block(1320, 560)
        block452 = Block(1360, 560)
        block453 = Block(1400, 560)
        block454 = Block(1440, 560)
        block455 = Block(1480, 560)
        block456 = Block(1520, 560)
        block457 = Block(1560, 560)
        block458 = Block(1600, 560)
        block459 = Block(1640, 560)
        block460 = Block(1680, 560)
        block461 = Block(1720, 560)
        block462 = Block(1760, 560)
        block463 = Block(1800, 560)
        block464 = Block(1840, 560)
        block465 = Block(1880, 560)
        block466 = Block(2000, 560)
        block467 = Block(2040, 560)
        block468 = Block(2080, 560)
        block469 = Block(2120, 560)
        block470 = Block(2160, 560)
        block471 = Block(2200, 560)
        block472 = Block(2240, 560)
        block473 = Block(2280, 560)
        block474 = Block(2320, 560)
        block475 = Block(2360, 560)
        block476 = Block(2400, 560)
        block477 = Block(2440, 560)
        block478 = Block(2480, 560)
        block479 = Block(2520, 560)
        block480 = Block(2560, 560)
        block481 = Block(2600, 560)
        block482 = Block(2640, 560)
        block483 = Block(2680, 560)
        block484 = Block(2720, 560)
        block485 = Block(2760, 560)
        block486 = Block(2800, 560)
        block487 = Block(2840, 560)
        block488 = Block(2880, 560)
        block489 = Block(2920, 560)
        block490 = Block(2960, 560)
        block491 = Block(3000, 560)
        block492 = Block(3040, 560)
        block493 = Block(3080, 560)
        block494 = Block(3120, 560)
        block495 = Block(3160, 560)
        block496 = Block(3200, 560)
        block497 = Block(3240, 560)
        block498 = Block(3280, 560)
        block499 = Block(3320, 560)
        block500 = Block(3360, 560)
        block501 = Block(3400, 560)
        block502 = Block(3440, 560)
        block503 = Block(3480, 560)
        block504 = Block(3520, 560)
        block505 = Block(3560, 560)
        block506 = Block(3600, 560)
        block507 = Block(3640, 560)
        block508 = Block(3680, 560)
        block509 = Block(3720, 560)
        block510 = Block(3760, 560)
        block511 = Block(3800, 560)
        block512 = Block(3840, 560)
        block513 = Block(3880, 560)
        block514 = Block(3920, 560)
        block515 = Block(3960, 560)
        block516 = Block(4000, 560)
        block517 = Block(4040, 560)
        block518 = Block(4080, 560)
        block519 = Block(4120, 560)
        block520 = Block(4160, 560)
        block521 = Block(4200, 560)
        block522 = Block(4240, 560)
        block523 = Block(4280, 560)
        block524 = Block(4320, 560)
        block525 = Block(4360, 560)
        block526 = Block(4400, 560)
        block527 = Block(4440, 560)
        block528 = Block(4480, 560)
        block529 = Block(4520, 560)
        block530 = Block(4560, 560)
        block531 = Block(4600, 560)
        block532 = Block(4640, 560)
        block533 = Block(4680, 560)
        block534 = Block(4720, 560)
        block535 = Block(4760, 560)
        block536 = Block(4800, 560)
        block537 = Block(4840, 560)
        block538 = Block(4880, 560)
        block539 = Block(4920, 560)
        block540 = Block(4960, 560)
        
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
                                        block300, block301, block302, block303,
                                        block304, block305, block306, block307,
                                        block308, block309, block310, block311,
                                        block312, block313, block314, block315,
                                        block316, block317, block318, block319,
                                        block320, block321, block322, block323,
                                        block324, block325, block326, block327,
                                        block328, block329, block330, block331,
                                        block332, block333, block334, block335,
                                        block336, block337, block338, block339,
                                        block340, block341, block342, block343,
                                        block344, block345, block346, block347,
                                        block348, block349, block350, block351,
                                        block352, block353, block354, block355,
                                        block356, block357, block358, block359,
                                        block360, block361, block362, block363,
                                        block364, block365, block366, block367,
                                        block368, block369, block370, block371,
                                        block372, block373, block374, block375,
                                        block376, block377, block378, block379,
                                        block380, block381, block382, block383,
                                        block384, block385, block386, block387,
                                        block388, block389, block390, block391,
                                        block392, block393, block394, block395,
                                        block396, block397, block398, block399,
                                        block400, block401, block402, block403,
                                        block404, block405, block406, block407,
                                        block408, block409, block410, block411,
                                        block412, block413, block414, block415,
                                        block416, block417, block418, block419,
                                        block420, block421, block422, block423,
                                        block424, block425, block426, block427,
                                        block428, block429, block430, block431,
                                        block432, block433, block434, block435,
                                        block436, block437, block438, block439,
                                        block440, block441, block442, block443,
                                        block444, block445, block446, block447,
                                        block448, block449, block450, block451,
                                        block452, block453, block454, block455,
                                        block456, block457, block458, block459,
                                        block460, block461, block462, block463,
                                        block464, block465, block466, block467,
                                        block468, block469, block470, block471,
                                        block472, block473, block474, block475,
                                        block476, block477, block478, block479,
                                        block480, block481, block482, block483,
                                        block484, block485, block486, block487,
                                        block488, block489, block490, block491,
                                        block492, block493, block494, block495,
                                        block496, block497, block498, block499,
                                        block500, block501, block502, block503,
                                        block504, block505, block506, block507,
                                        block508, block509, block510, block511,
                                        block512, block513, block514, block515,
                                        block516, block517, block518, block519,
                                        block520, block521, block522, block523,
                                        block524, block525, block526, block527,
                                        block528, block529, block530, block531,
                                        block532, block533, block534, block535,
                                        block536, block537, block538, block539,
                                        block540)
        

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
