import pygame
import init


class Sound():

    def __init__(self, state):
        self.music = init.MUSIC
        self.game_state = state
        self.set_music()

    def set_music(self):
        """Sets music for level"""
        if self.game_state == "FOREST":
            pygame.mixer.music.load(self.music['forest'])
            pygame.mixer.music.play()

        elif self.game_state == "CITY":
            pygame.mixer.music.load(self.music['city'])
            pygame.mixer.music.play()

        elif self.game_state == "PARK":
            pygame.mixer.music.load(self.music['park'])
            pygame.mixer.music.play()
