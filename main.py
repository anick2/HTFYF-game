import sys
import pygame
import levels.forest
import levels.city
import levels.state
import levels.park
import levels.main_menu
import init


STATES = {"MAIN_MENU": levels.main_menu.MainMenu(),
          "FOREST": levels.forest.Forest(),
          "CITY": levels.city.City(),
          "PARK": levels.park.Park(),
          "CHOOSE_HERO": levels.main_menu.Hero_Choice(),
          "LOOSE_GAME": levels.main_menu.End()}


class Game:
    def __init__(self):
        self.screen = init.screen
        self.keys = pygame.key.get_pressed()
        self.done = False
        self.fps = 60
        self.state_name = None
        self.state = None

    def setup_states(self, start_state):
        self.state_name = start_state
        self.state = STATES[start_state]

    def update(self):
        self.keys = pygame.key.get_pressed()
        if self.state.done:
            self.flip_state()
        self.state.on_update(self.keys)

    def rebirth(self, state_name):
        if state_name == "FOREST":
            STATES[state_name] = levels.forest.Forest()
        elif state_name == "CITY":
            STATES[state_name] = levels.city.City()
        elif state_name == "PARK":
            STATES[state_name] = levels.park.Park()
        elif state_name == "MAIN_MENU":
            STATES[state_name] = levels.main_menu.MainMenu()
        elif state_name == "LOOSE_GAME":
            STATES[state_name] = levels.main_menu.End()
        if state_name == "CHOOSE_HERO":
            STATES[state_name] = levels.main_menu.Hero_Choice()

    def flip_state(self):
        prev = self.state_name
        self.state_name = STATES[self.state_name].next_state
        self.state = STATES[self.state_name]
        self.state.on_create()
        self.rebirth(prev)

    def event_loop(self):
        for event in pygame.event.get():
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

            self.state.get_event(event)

    def start(self):
        self.state.on_create()
        self.mainloop()

    def mainloop(self):
        while not self.done:
            self.event_loop()
            self.update()
        self.clock.tick(self.fps)


def main():
    game = Game()
    first_state = "MAIN_MENU"
    game.setup_states(first_state)
    game.start()


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
