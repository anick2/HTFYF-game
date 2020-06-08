import pygame
import os

accept_graphics = ('.png', '.jpg', '.bmp')
accept_music = ('.wav', '.mp3', '.ogg', '.mdi')

def load_graphics(directory):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept_graphics:
            img = pygame.image.load(os.path.join(directory, pic))
            img = img.convert()
            graphics[name] = img
    return graphics

def load_music(directory):
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept_music:
            songs[name] = os.path.join(directory, song)
    return songs
