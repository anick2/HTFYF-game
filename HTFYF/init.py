import pygame
import const as c
import load
import os
import gettext


path_prefix = os.path.dirname(os.path.abspath(__file__))
print(path_prefix)
gettext.install("locale", path_prefix)
pygame.init()
pygame.display.set_caption(c.CAPTION)
screen = pygame.display.set_mode(c.SCREEN_SIZE)
screen_rect = screen.get_rect()

IMAGES = load.load_graphics(os.path.join(path_prefix, "sources",
							_("images")))
MUSIC = load.load_music(os.path.join(path_prefix, "sources",
						"music"))
