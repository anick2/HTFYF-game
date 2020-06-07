import pygame
from state import *
from init import *

class Park(State):          # класс для состояния "парк"
    def __init__(self):
        State.__init__(self)
        self.on_create();   
        
    def on_create(self):      
        pygame.display.flip()
        screen.blit(IMAGES["park"], screen_rect)

    def on_update(self):
        pygame.display.flip()
        screen.blit(IMAGES["park"], screen_rect)

    def get_event(self, event):
        pass
