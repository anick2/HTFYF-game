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
        pygame.draw.rect(screen,(255,255,255),(500,300,100,50));

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True
