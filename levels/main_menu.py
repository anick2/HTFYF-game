import sys
import pygame
from .state import *

sys.path.append('..')

from init import *
import const


# класс для состояния "меню"
class MainMenu(State):        
    def __init__(self):
        State.__init__(self)
        self.next_state = "CHOOSE_HERO"

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
        self.next_state = "FOREST"

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
        pygame.draw.rect(screen, (255, 255, 255), (600, 800, 400, 200))

        self.image_first = pygame.transform.scale(IMAGES["walk1"], (100, 100))
        self.image_first.set_colorkey((0, 0, 0))
        screen.blit(self.image_first, (750, 350))

        pygame.draw.rect(screen, (255, 255, 255), (200, 400, 400, 200))

        self.image_second = pygame.transform.scale(IMAGES["walk1s"], (100, 100))
        self.image_second.set_colorkey((0, 0, 0))
        screen.blit(self.image_second, (350, 350))

        self.image_choose = pygame.transform.scale(IMAGES["choose"], c.CHOOSE_SIZE)
        self.image_choose.set_colorkey((0, 0, 0))
        screen.blit(self.image_choose, (c.WIDTH / 2 - c.CHOOSE_WIDTH / 2, 0))

        self.image_start = pygame.transform.scale(IMAGES["start_button"], c.START_SIZE)
        self.image_start.set_colorkey((0,0,0))

        self.hero1 = 1
        self.hero2 = 0
        c.HERO_TYPE = 's'

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

        pygame.draw.rect(screen, (self.hero2 * 255, self.hero2 * 255, self.hero2 * 255), (300, 300, 200, 200))
        pygame.draw.rect(screen, (self.hero1 * 255, self.hero1 * 255, self.hero1 * 255), (50, 300, 200, 200))


        #self.image_first.set_colorkey((0, 0, 0))
        screen.blit(self.image_first, (350, 350))

        

        #self.image_second.set_colorkey((0, 0, 0))
        screen.blit(self.image_second, (100, 350))

        #self.image_choose.set_colorkey((0, 0, 0))
        screen.blit(self.image_choose, (c.WIDTH / 2 - c.CHOOSE_WIDTH / 2, 0))
        
        screen.blit(self.image_start, (c.WIDTH / 2, c.HEIGHT - c.START_HEIGHT))

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= c.WIDTH / 2 and pygame.mouse.get_pos()[1] >= c.HEIGHT - c.START_HEIGHT:
                if pygame.mouse.get_pos()[0] <= c.WIDTH / 2 + c.START_WIDTH and pygame.mouse.get_pos()[1] <= c.HEIGHT:
                    self.done = True
            if pygame.mouse.get_pos()[0] >= 50 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 500:
                    self.hero1 = 1
                    self.hero2 = 0
                    c.HERO_TYPE = 's'
            if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[1] <= 500:
                    self.hero1 = 0
                    self.hero2 = 1
                    c.HERO_TYPE = ''



class End(State):        
    def __init__(self):
        State.__init__(self)
        self.next_state = "MAIN_MENU"

    def on_create(self):
        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.image.fill((0, 0, 0))
        self.counter = 0
        self.color = pygame.Color('yellow')
        self.font = pygame.font.SysFont( 'meslolgmboldforpowerlinettf', 30)
        self.fl = -1
        self.fp = 0
        self.pow = 0.3

    def on_update(self, keys):
        pygame.display.flip()

        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.image.fill((0, 0, 0))
        
        if self.counter < const.COINS and self.fp == 2:
            self.fp = 0
            self.counter += 1

        self.fp += 1
            
        over = self.font.render("GAME OVER :( ", True, self.color)
        fon = self.font.render("Total: " + str(self.counter), True, self.color)
        menu = self.font.render("Main Menu" , True, self.color)
        ret = self.font.render("Try Again" , True, self.color)
        
        fon_rect = fon.get_rect()

        pygame.draw.rect(self.image, (self.pow * 255, self.pow * 255, self.pow * 255), (700, 300, ret.get_rect().width, ret.get_rect().height))
        pygame.draw.rect(self.image, ((1 - self.pow) * 255, (1 - self.pow) * 255, (1 - self.pow) * 255), (200, 300, menu.get_rect().width, menu.get_rect().height))

        self.image.blit(over, (400, 100))
        self.image.blit(fon, (400, 200))
        self.image.blit(menu, (200, 300))
        self.image.blit(ret, (700, 300))
        screen.blit(self.image, (0, 0))



    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 300 and pygame.mouse.get_pos()[1] <= 350:
                    self.pow = 1 - self.pow
                    self.next_state = "MAIN_MENU"
                    if self.fl == 1:
                        self.done = True
                    self.fl = 1
                    
            if pygame.mouse.get_pos()[0] >= 700 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 800 and pygame.mouse.get_pos()[1] <= 350:
                    self.pow = 1 - self.pow
                    self.next_state = "FOREST"
                    if self.fl == 0:
                        self.done = True
                    self.fl = 0
    
                    
