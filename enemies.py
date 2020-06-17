import pygame
import main
import const as c
from init import *


class Enemy(pygame.sprite.Sprite):
    """Base class for all enemies """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def setup_enemy(self, x, y, direction, name, setup_frames, state):
        """Sets up various values for enemy"""
        self.frames = []
        self.frame_index = 0
        self.death_timer = 0
        self.state = state 

        self.name = name
        self.direction = direction
        setup_frames()
        self.image = pygame.Surface(c.HERO_SIZE).convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()

    def set_velocity(self):
    	""" Устанавливает вектор скорости в зависимости от направления"""
    	pass

    def get_image(self, img, width, height):
        """Get the image frames from the sprite sheet"""
        image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(img, (0, 0))
        image.set_colorkey((0,0,0))

        return image

    def update(self, game_info, *args):
        """Updates enemy behavior"""
        #self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.animation()

    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == "WALK":
            self.walking()
        '''elif self.state == "FALL":
            self.falling()
        elif self.state == "JUMPED_ON":
            self.jumped_on()
        elif self.state == "SHELL_SLIDE":
            self.shell_sliding()
        elif self.state == "DEATH_JUMP":
            self.death_jumping()'''

    def walking(self):
        if self.frame_index < 2:
            self.frame_index += 1
        else:
            self.frame_index = 0

    def animation(self):
        self.image.blit(self.frames[self.frame_index], (0, 0))


class Mushroom(Enemy):

    def __init__(self, x=300, y= c.HEIGHT - c.HEIGHT_OF_GROUND, direction='left', name='mushroom', state = 'WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 1
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY
        

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frame_index = 0

        self.frames = []

        for i in range(1, 7):
            img = pygame.transform.scale(IMAGES["m_walk_" + str(i)], c.HERO_SIZE)                       
            self.frames.append(img)


class Spider(Enemy):

    def __init__(self, x=300, y= c.HEIGHT - c.HEIGHT_OF_GROUND, direction='left', name='mushroom', state = 'WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 2
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY
        

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frame_index = 0

        self.frames = []

        for i in range(1, 5):
            img = pygame.transform.scale(IMAGES["b_walk_" + str(i)], c.HERO_SIZE)                       
            self.frames.append(img)

class Cop(Enemy):

    def __init__(self, x=300, y= c.HEIGHT - c.HEIGHT_OF_GROUND, direction='left', name='mushroom'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frame_index = 0

        self.frames = []

        for i in range(1, 4):
            img = pygame.transform.scale(IMAGES["left_" + str(i)], c.HERO_SIZE)                       
            self.frames.append(img)

class Granny(Enemy):

    def __init__(self, x=300, y= c.HEIGHT - c.HEIGHT_OF_GROUND, direction='left', name='mushroom'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frame_index = 0

        self.frames = []

        for i in range(1, 4):
            img = pygame.transform.scale(IMAGES["left_" + str(i)], c.HERO_SIZE)                       
            self.frames.append(img)

class Bear(Enemy):

    def __init__(self, x=300, y= c.HEIGHT - c.HEIGHT_OF_GROUND, direction='left', name='mushroom'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frame_index = 0

        self.frames = []

        for i in range(1, 4):
            img = pygame.transform.scale(IMAGES["left_" + str(i)], c.HERO_SIZE)                       
            self.frames.append(img)

class Clown(Enemy):

    def __init__(self, x=300, y= c.HEIGHT - c.HEIGHT_OF_GROUND, direction='left', name='mushroom'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        

    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        self.frame_index = 0

        self.frames = []

        for i in range(1, 4):
            img = pygame.transform.scale(IMAGES["left_" + str(i)], c.HERO_SIZE)                       
            self.frames.append(img)
            
    '''def jumped_on(self):
        """When Mario squishes him"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()'''
