import sys
import pygame
import const as c
from levels.forest import *
from levels.city import *
from levels.state import *
from levels.park import *
from levels.main_menu import *
from init import *


STATES = {"MAIN_MENU": MainMenu(),
              "FOREST": Forest(),
              "CITY": City(),
              "PARK": Park(),
              "CHOOSE_HERO": Hero_Choice(),
              "LOOSE_GAME": End()}   

class Game:
    def __init__(self):
        self.screen = screen
        self.keys = pygame.key.get_pressed()
        self.done = False                   #конец игры
        self.fps = 60
        self.state_name = None              #имя текущего состояния
        self.state = None                   #объект класса текущего состояния
        
    def setup_states(self, start_state):
        '''инициализация состояний'''
        self.state_name = start_state
        self.state = STATES[start_state]

    def update(self):
        self.keys = pygame.key.get_pressed()
        if self.state.done:
            self.flip_state()
        self.state.on_update(self.keys)


    def rebirth(self, state_name):
        if state_name == "FOREST":
            STATES[state_name] = Forest()
        elif state_name == "CITY":
            STATES[state_name] = City()
        elif state_name == "PARK":
            STATES[state_name] = Park()
        elif state_name == "MAIN_MENU":
            STATES[state_name] = MainMenu()
        elif state_name == "LOOSE_GAME":
            STATES[state_name] = End()
        if state_name == "CHOOSE_HERO":
            STATES[state_name] = Hero_Choice()

    def flip_state(self):
        # смена состояний
        prev = self.state_name
        self.state_name = STATES[self.state_name].next_state
        self.state = STATES[self.state_name]
        self.state.on_create()
        self.rebirth(prev)
    
    def event_loop(self):
        for event in pygame.event.get():
            # нужно написать обработку событий
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self = False

            if event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    self = False

            self.state.get_event(event);
            
    def start(self):
        # запуск первого состояния
        self.state.on_create();
        # запуск мэйнлупа
        self.mainloop();
        

    def mainloop(self):
        while not self.done:
            self.event_loop()
            self.update()
        self.clock.tick(self.fps) 
        


def main():
    game = Game()
    first_state = "MAIN_MENU"                        # начальное состояние
    game.setup_states(first_state)           # установка состояний
    game.start()                                     # начало игры
    
if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
