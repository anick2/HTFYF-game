import pygame
import main
import const as c
from init import *


class Enemy(pygame.sprite.Sprite):
    """Base class for all enemies """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Sets up various values for enemy"""
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = "STAND" 

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
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
        self.current_time = game_info[c.CURRENT_TIME]
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

    '''def walking(self):
    """Default state of moving sideways"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.animate_timer = self.current_time

 	def falling(self):
        """For when it falls off a ledge"""
        if self.y_vel < 10:
            self.y_vel += self.gravity


	def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass


    def death_jumping(self):
        """Death animation"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()


    def start_death_jump(self, direction):
        """Transitions enemy into a DEATH JUMP state"""
        self.y_vel = -8
        if direction == c.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = c.DEATH_JUMP'''


    def animation(self):
        """Basic animation, switching between two frames"""
        self.image = self.frames[self.frame_index]


class Mushroom(Enemy):

    def __init__(self, y=c.HEIGHT_OF_GROUND, x=0, direction='left', name='mushroom'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Put the image frames in a list to be animated"""

        for i in range(1, 4):
            img = pygame.transform.scale(IMAGES["left_" + str(i)], (150, 200))                       
            self.frames.append(self.get_image(img, 30, 50))


    '''def jumped_on(self):
        """When Mario squishes him"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()'''