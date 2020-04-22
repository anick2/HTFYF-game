import sys
import pygame
import const as c
import os
import load

def init():
    global screen, screen_rect, IMAGES
    pygame.init()
    pygame.display.set_caption(c.CAPTION)
    screen = pygame.display.set_mode(c.SCREEN_SIZE)
    IMAGES = load.load_graphics(os.path.join("sourses","images"))
    screen_rect = screen.get_rect()

class Game:
    def __init__(self):
        self.screen = screen
        #self.clock = pygame.time.Clock()
        #self.current_time = 0.0
        self.keys = pygame.key.get_pressed()
        self.done = False                   #конец игры
        self.fps = 60
        self.state_dict = {}                #словарь всевозможных состояний
        self.state_name = None              #имя текущего состояния
        self.state = None                   #объект класса текущего состояния
        
    def setup_states(self, state_dict, start_state):
        '''инициализация состояний'''
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[start_state]

    def update(self):
        #self.current_time = pygame.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        '''смена состояний'''
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous
    
    def event_loop(self):
        for event in pygame.event.get():
            '''нужно написать обработку событий'''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    self = False
                      
    def start(self):
        '''mainloop'''
        while not self.done:
            self.event_loop()
            pygame.display.flip()
            screen.blit(IMAGES["menu"], screen_rect)
        self.clock.tick(self.fps)
        


class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass

def main():
    init()
    game = Game()
    states = {} # словаь состояний {"MAIN_MENU": MainMenu()}
    #first_state = "MAIN_MENU"
    #game.setup_states(states, first_state)
    game.start()
    
if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
