import sys
import pygame
from pygame.locals import *
import const as c
import os
import load

COLOR_RED = (255,0,0)
COLOR_BLACK = (255,255,255)

def init():
    global screen, screen_rect, IMAGES, start_button, continue_button, quit_button, border_color
    pygame.init()
    pygame.display.set_caption(c.CAPTION)
    screen = pygame.display.set_mode(c.SCREEN_SIZE, HWSURFACE | DOUBLEBUF | RESIZABLE)
    IMAGES = load.load_graphics(os.path.join("sources","images"))
    border_color = (0,0,0)
    #start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
    #continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
    screen_rect = screen.get_rect()

class Game:
    def __init__(self):
        self.screen = screen
        self.clock = pygame.time.Clock()
        #self.current_time = 0.0
        #self.keys = pg.key.get_pressed()   
        self.done = False                   #конец игры
        self.fps = 7
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
            if event.type == pygame.MOUSEMOTION:
                if pygame.Rect(450,350,100,50).collidepoint(event.pos[0] - 450,
                                event.pos[1] - 350):
                    border_color = COLOR_RED
                else:
                    border_color = COLOR_BLACK

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    self = False
            if event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(
                event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                screen.blit(pygame.transform.scale(IMAGES["fon"], event.dict['size']), (0, 0))
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 450 and pygame.mouse.get_pos()[1] >= 350:
                    if pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] <= 400:
                        pygame.quit()
                        sys.exit()
                        self = False
                      
    def start(self):
        '''mainloop'''
        i = 0
        while not self.done:
            self.event_loop()
            imag = "fon" + str(i)
            screen.blit(pygame.transform.scale(IMAGES[imag], c.SCREEN_SIZE), screen_rect)
            #button_surf = pygame.transform.scale(IMAGES["button"], (100,50))
            #button_rect = button_surf.get_rect()
            #screen.blit(button_surf, (450,350))
            pygame.draw.rect(screen,border_color,(450,350,100,50));
            pygame.display.flip()
            self.clock.tick(self.fps)
            i = (i+1) % 8
        


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
