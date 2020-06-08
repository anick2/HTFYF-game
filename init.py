import pygame
import const as c
import load
import os


pygame.init()
pygame.display.set_caption(c.CAPTION)
screen = pygame.display.set_mode(c.SCREEN_SIZE)
#start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
#continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
screen_rect = screen.get_rect()


IMAGES = load.load_graphics(os.path.join("sources","images"))
MUSIC = load.load_music(os.path.join("sources","music"))

