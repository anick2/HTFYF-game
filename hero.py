import pygame
import main
import const as c
from init import *


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.hero_type = c.HERO_TYPE            #персонаж, которого выбрал игрок
        self.state = "STAND"                    #текущее состояние героя
        self.facing_right = True                #куда смотрит
        self.allow_jump = True
        self.allow_hit = True
        self.frame_index = 0
        self.pos_x = 100

        
        self.load_images()
        
        img = self.right_frames[self.frame_index]
        self.image = pygame.Surface(c.HERO_SIZE).convert()
        self.image.set_colorkey((0,0,0))
        self.image_rect = self.image.get_rect()
        self.image.blit(img, (0, 0))

        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)



    def load_images(self):
        self.left_walking = []
        self.right_walking = []

        self.left_fighting = []
        self.right_fighting = []

        for i in range(1, 9):
            img = pygame.transform.scale(IMAGES["walk" + str(i)], c.HERO_SIZE)                       
            self.right_walking.append(img)


        self.right_fighting.append(IMAGES["hit1"])
        self.right_fighting.append(IMAGES["hit2"])

        for image in self.right_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.left_walking.append(new_image)

        for image in self.right_fighting:
            new_image = pygame.transform.flip(image, True, False)
            self.left_fighting.append(new_image)


        self.right_frames = self.right_walking
        self.left_frames = self.left_walking

        #self.all_images = [left_walking, right_walking, left_fighting, right_fighting]


    def update(self, keys, fire_group):    

        self.handle_state(keys, fire_group)
        self.animation()

    def handle_state(self, keys, fire_group):
        
        if self.state == "STAND":
            self.standing(keys, fire_group)
            
        elif self.state == "WALK":
            self.walking(keys, fire_group)
            
        elif self.state == "JUMP":
            self.jumping(keys, fire_group)
            
        elif self.state == "FALL":
            self.falling(keys, fire_group)

            
    def standing(self, keys, fire_group):
        self.frame_index = 0

        if keys[pygame.K_d]:
            self.state = "WALK"
            self.facing_right = True


        if keys[pygame.K_a]:
            self.state = "WALK"
            self.facing_right = False
            
  


    def walking(self, keys, fire_group):

        if self.frame_index == 0:
            self.frame_index += 1

        else:
            if self.frame_index < 7:
                self.frame_index += 1
            else:
                self.frame_index = 0

        if keys[pygame.K_d]:
            self.facing_right = True
            self.pos_x += 7

        if keys[pygame.K_a]:
            self.facing_right = False
            self.pos_x -= 7
  


    def animation(self):
        if self.facing_right:
            img = self.right_frames[self.frame_index]
            self.image.blit(img, (0,0))
        else:
            img = self.left_frames[self.frame_index]
            self.image.blit(img, (0,0))


    def calculate_animation_speed(self):
        pass
    
