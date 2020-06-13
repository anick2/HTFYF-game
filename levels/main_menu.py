import sys
import pygame
from .state import *

sys.path.append('..')

from init import *


# класс для состояния "меню"
class MainMenu(State):        
    def __init__(self):
        State.__init__(self)
        self.on_create();

    def on_create(self):
        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.image_name = pygame.transform.scale(IMAGES["name_text"], c.TEXT_SIZE)
        self.image_name.set_colorkey((0, 0, 0))
        self.image_start = pygame.transform.scale(IMAGES["start_button"], c.START_SIZE)
        self.image_start.set_colorkey((0,0,0))
        self.background = []
        self.clock = 0
        pygame.display.flip()
        #изображение:
        for i in range(1, 7):
            img = pygame.transform.scale(IMAGES["main_bg" + str(i)], c.SCREEN_SIZE)                       
            self.background.append(img)
        self.background_index = 0;
        self.clock = 1
        self.image.blit(IMAGES["main_bg1"], (0, 0))
        screen.blit(self.image, (0, 0))
        screen.blit(self.image_name, (c.WIDTH / 2 - c.TEXT_WIDTH / 2, 0))
        screen.blit(self.image_start, (c.WIDTH / 2, c.HEIGHT - c.START_HEIGHT))

    def on_update(self, keys):
        pygame.display.flip()
        if self.clock == 25:
            if self.background_index < 5:
                self.background_index += 1
            else:
                self.background_index = 0
            self.clock = 0
        else:
            self.clock += 1

        self.image.blit(self.background[self.background_index], (0, 0))
        screen.blit(self.image, (0, 0))
        screen.blit(self.image_name, (c.WIDTH / 2 - c.TEXT_WIDTH / 2, 0))
        screen.blit(self.image_start, (c.WIDTH / 2, c.HEIGHT - c.START_HEIGHT))

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= c.WIDTH / 2 and pygame.mouse.get_pos()[1] >= c.HEIGHT - c.START_HEIGHT:
                if pygame.mouse.get_pos()[0] <= c.WIDTH / 2 + c.START_WIDTH and pygame.mouse.get_pos()[1] <= c.HEIGHT:
                    self.done = True







class Hero_Choice(State):        
    def __init__(self):
        State.__init__(self)
        self.on_create();

    def on_create(self):
        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.background = []
        self.clock = 0
        pygame.display.flip()
        #изображение:
        for i in range(1, 7):
            img = pygame.transform.scale(IMAGES["main_bg" + str(i)], c.SCREEN_SIZE)                       
            self.background.append(img)
        self.background_index = 0;
        self.clock = 1
        self.image.blit(IMAGES["main_bg1"], (0, 0))
        screen.blit(self.image, (0, 0))
        
        self.surf1 = pygame.Surface((250, 300)).convert()
        self.surf2 = pygame.Surface(c.HERO_SIZE).convert()
        self.surf3 = pygame.Surface(c.HERO_SIZE).convert()

        img1 = pygame.transform.scale(IMAGES["hero2"], (250, 300))
        img2 = pygame.transform.scale(IMAGES["hero1"], (250, 300))
        img3 = pygame.transform.scale(IMAGES["choose"], (500, 100)) 

        self.surf1.blit(img1, (0, 0))
        self.surf2.blit(img2, (0, 0))
        self.surf3.blit(img3, (0, 0))
        
        pygame.draw.rect(screen,(255,255,255),(500,300,100,50));

    def on_update(self, keys):
        pygame.display.flip()
        if self.clock == 25:
            if self.background_index < 5:
                self.background_index += 1
            else:
                self.background_index = 0
            self.clock = 0
        else:
            self.clock += 1

        self.image.blit(self.background[self.background_index], (0, 0))
        screen.blit(self.image, (0, 0))

        screen.blit(self.surf1, (166,200))
        screen.blit(self.surf2, (582,300))
        screen.blit(self.surf3, (50,100))
        
        pygame.draw.rect(screen,(255,255,255),(500,300,100,50));

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True

