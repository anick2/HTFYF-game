import pygame
import os

accept=('.png', '.jpg', '.bmp', '.gif')

def load_graphics(directory):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey((255,255,255))
            graphics[name] = img
    return graphics
