import sys
import pygame
import const as c
import os
import load

def init():
    global screen, screen_rect, IMAGES, start_button, continue_button, quit_button
    pygame.init()
    pygame.display.set_caption(c.CAPTION)
    screen = pygame.display.set_mode(c.SCREEN_SIZE)
    IMAGES = load.load_graphics(os.path.join("sources","images"))
    #start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
    #continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
    screen_rect = screen.get_rect()

class Game:
    def __init__(self):
        self.screen = screen
        #self.keys = pg.key.get_pressed()   
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
        if self.state.done:
            self.flip_state()
        self.state.on_update()

    def flip_state(self):
        # смена состояний
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.on_create()
    
    def event_loop(self):
        for event in pygame.event.get():
            # нужно написать обработку событий
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self = False

            if event.type == pygame.KEYDOWN:
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
        


class State:
    def __init__(self):
        self.done     = False # состояние завершилось
        self.next     = None  # следубщее состояние
        self.prev     = None  # предудущее состояние

    # запускается при создании
    def on_create(self):
        pass

    # запускается @fps раз в секунду для обновления
    def on_update(self):
        pass

    # запускается для отлова ивентов
    def get_event(self, event):
        pass

    # задаем соседние состояния
    def set_prenex(self, pre, nex):
        self.next = nex;
        self.prev = pre;
    

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

    def on_update(self):
        pygame.display.flip()
        screen.blit(IMAGES["menu"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(500,300,100,50));

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True
    
# класс для состояния "лес"
class Forest(State):          
    def __init__(self):
        State.__init__(self)
        self.on_create();   
        
    def on_create(self):      
        pygame.display.flip()
        screen.blit(IMAGES["forest"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));

    def on_update(self):
        pygame.display.flip()
        screen.blit(IMAGES["forest"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(600,300,100,50));

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True

# класс для состояния "город"
class City(State):          
    def __init__(self):
        State.__init__(self)
        self.on_create();   
        
    def on_create(self):      
        pygame.display.flip()
        screen.blit(IMAGES["city"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(400,300,100,50));

    def on_update(self):
        pygame.display.flip()
        screen.blit(IMAGES["city"], screen_rect)
        pygame.draw.rect(screen,(255,255,255),(400,300,100,50));

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[1] <= 350:
                    self.done = True

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

def main():
    init()
    game = Game()
    states = {"MAIN_MENU": MainMenu(),
              "FOREST": Forest(),
              "CITY": City(),
              "PARK": Park()}                        # словарь состояний 
    first_state = "MAIN_MENU"                        # начальное состояние
    states["MAIN_MENU"].set_prenex(None, "FOREST")   # объявление состояний
    states["FOREST"].set_prenex("MAIN_MENU", "CITY") 
    states["CITY"].set_prenex("FOREST", "PARK")
    states["PARK"].set_prenex("PARK", None)
    game.setup_states(states, first_state)           # установка состояний
    game.start()                                     # начало игры
    
if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
