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
        pygame.display.flip()
        #изображение:
        screen.blit(IMAGES["menu"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(500,300,100,50));

    def on_update(self, keys):
        pygame.display.flip()
        screen.blit(IMAGES["menu"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(500,300,100,50));

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True
