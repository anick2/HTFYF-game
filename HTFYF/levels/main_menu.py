import sys
import pygame
from .state import State
import init
import const as c
from sounds import Sound

sys.path.append('..')


class MainMenu(State):
    """Class Main menu"""
    def __init__(self):
        """Initializes the state"""
        State.__init__(self)
        self.next_state = "CHOOSE_HERO"

    def on_create(self):
        """Called every time the game's state becomes this one.  Initializes
        certain values"""
        self.sound_player = Sound("MAIN_MENU")
        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.image_name = pygame.transform.scale(init.IMAGES["name_text"],
                                                 c.TEXT_SIZE)
        self.image_name.set_colorkey((0, 0, 0))
        self.image_start = pygame.transform.scale(init.IMAGES["start_button"],
                                                  c.START_SIZE)
        self.image_start.set_colorkey((0, 0, 0))
        self.background = []
        self.clock = 0
        pygame.display.flip()
        for i in range(1, 7):
            img = pygame.transform.scale(init.IMAGES["main_bg" + str(i)],
                                         c.SCREEN_SIZE)
            self.background.append(img)
        self.background_index = 0
        self.clock = 1
        self.image.blit(init.IMAGES["main_bg1"], (0, 0))
        init.screen.blit(self.image, (0, 0))
        init.screen.blit(self.image_name, (c.WIDTH / 2 - c.TEXT_WIDTH / 2, 0))
        init.screen.blit(self.image_start, (c.WIDTH / 2,
                                            c.HEIGHT - c.START_HEIGHT))

    def on_update(self, keys):
        """Updates the state every refresh"""
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
        init.screen.blit(self.image, (0, 0))
        init.screen.blit(self.image_name, (c.WIDTH / 2 - c.TEXT_WIDTH / 2, 0))
        init.screen.blit(self.image_start, (c.WIDTH / 2,
                                            c.HEIGHT - c.START_HEIGHT))

    def get_event(self, event):
        """Creates a button - character selection"""
        t1 = c.HEIGHT - c.START_HEIGHT
        t2 = c.WIDTH / 2 + c.START_WIDTH
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= c.WIDTH / 2:
                if pygame.mouse.get_pos()[1] >= t1:
                    if pygame.mouse.get_pos()[0] <= t2:
                        if pygame.mouse.get_pos()[1] <= c.HEIGHT:
                            self.done = True


class Hero_Choice(State):
    """Class hero choice"""
    def __init__(self):
        State.__init__(self)
        self.next_state = "FOREST"

    def on_create(self):
        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.background = []
        self.clock = 0
        pygame.display.flip()
        for i in range(1, 7):
            img = pygame.transform.scale(init.IMAGES["main_bg"
                                         + str(i)], c.SCREEN_SIZE)
            self.background.append(img)
        self.background_index = 0
        self.clock = 1
        self.image.blit(init.IMAGES["main_bg1"], (0, 0))
        init.screen.blit(self.image, (0, 0))
        pygame.draw.rect(init.screen, (255, 255, 255), (600, 800, 400, 200))

        self.click1 = False
        self.click2 = False

        self.image_first = pygame.transform.scale(init.IMAGES["pers_1"],
                                                  (280, 400))
        self.image_first.set_colorkey((0, 0, 0))
        init.screen.blit(self.image_first, (750, 350))

        pygame.draw.rect(init.screen, (255, 255, 255), (200, 400, 400, 200))

        self.image_second = pygame.transform.scale(init.IMAGES["pers_2"],
                                                   (280, 400))
        self.image_second.set_colorkey((0, 0, 0))
        init.screen.blit(self.image_second, (350, 350))

        self.image_choose = pygame.transform.scale(init.IMAGES["choose"],
                                                   c.CHOOSE_SIZE)
        self.image_choose.set_colorkey((0, 0, 0))
        init.screen.blit(self.image_choose, (c.WIDTH / 2 - c.CHOOSE_WIDTH / 2,
                                             0))
        self.surf = pygame.Surface((280, 400))
        self.surf.set_alpha(128)
        self.surf.fill((200, 162, 200))
        self.hero1 = 1
        self.hero2 = 0
        c.HERO_TYPE = 's'

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
        init.screen.blit(self.image, (0, 0))

        if self.click1:
            init.screen.blit(self.surf, (20, 100))

        if self.click2:
            init.screen.blit(self.surf, (700, 100))

        init.screen.blit(self.image_first, (20, 100))

        init.screen.blit(self.image_second, (710, 100))

        init.screen.blit(self.image_choose,
                         (c.WIDTH / 2 - c.CHOOSE_WIDTH / 2,
                          c.HEIGHT / 2 - c.CHOOSE_HEIGHT / 2))

    def get_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pos()[0] >= 20:
                if pygame.mouse.get_pos()[1] >= 100:
                    if pygame.mouse.get_pos()[0] <= 300:
                        if pygame.mouse.get_pos()[1] <= 500:
                            self.hero1 = 1
                            self.hero2 = 0
                            c.HERO_TYPE = ''
                            self.click2 = False
                            if self.click1:
                                self.done = True
                            self.click1 = True

            if pygame.mouse.get_pos()[0] >= 700:
                if pygame.mouse.get_pos()[1] >= 100:
                    if pygame.mouse.get_pos()[0] <= 980:
                        if pygame.mouse.get_pos()[1] <= 500:
                            self.hero1 = 0
                            self.hero2 = 1
                            c.HERO_TYPE = 's'
                            self.click1 = False
                            if self.click2:
                                self.done = True
                            self.click2 = True


class End(State):
    def __init__(self):
        State.__init__(self)
        self.next_state = "MAIN_MENU"

    def on_create(self):
        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.image.fill((0, 0, 0))
        self.counter = 0
        self.color = pygame.Color('yellow')
        self.font = pygame.font.SysFont('meslolgmboldforpowerlinettf', 30)
        self.fl = -1
        self.fp = 0
        self.pow = 0.3

    def on_update(self, keys):
        pygame.display.flip()

        self.image = pygame.Surface(c.SCREEN_SIZE).convert()
        self.image.fill((0, 0, 0))

        if self.counter < c.COINS and self.fp == 2:
            self.fp = 0
            self.counter += 1

        self.fp += 1
        over = self.font.render("GAME OVER :( ", True, self.color)
        fon = self.font.render("Total: " + str(self.counter), True, self.color)
        menu = self.font.render("Main Menu", True, self.color)
        ret = self.font.render("Try Again", True, self.color)

        pygame.draw.rect(self.image, (self.pow * 255, self.pow * 255,
                                      self.pow * 255),
                                     (700, 300, ret.get_rect().width,
                                      ret.get_rect().height))

        pygame.draw.rect(self.image, ((1 - self.pow) * 255,
                         (1 - self.pow) * 255, (1 - self.pow) * 255),
                         (200, 300, menu.get_rect().width,
                         menu.get_rect().height))

        self.image.blit(over, (400, 100))
        self.image.blit(fon, (400, 200))
        self.image.blit(menu, (200, 300))
        self.image.blit(ret, (700, 300))
        init.screen.blit(self.image, (0, 0))

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pos()[0] >= 200:
                if pygame.mouse.get_pos()[1] >= 300:
                    if pygame.mouse.get_pos()[0] <= 300:
                        if pygame.mouse.get_pos()[1] <= 350:
                            self.pow = 1 - self.pow
                            self.next_state = "MAIN_MENU"
                            if self.fl == 1:
                                self.done = True
                            self.fl = 1

            if pygame.mouse.get_pos()[0] >= 700:
                if pygame.mouse.get_pos()[1] >= 300:
                    if pygame.mouse.get_pos()[0] <= 800:
                        if pygame.mouse.get_pos()[1] <= 350:
                            self.pow = 1 - self.pow
                            self.next_state = "FOREST"
                            if self.fl == 0:
                                self.done = True
                            self.fl = 0
