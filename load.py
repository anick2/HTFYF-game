import pygame
import os

accept=('.png', 'jpg', 'bmp')

def load_graphics(directory):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            img = img.convert()
            graphics[name] = img
    return graphics



def get_graphics():
    global IMAGES
    IMAGES = load_graphics(os.path.join("sources","images"))
    
