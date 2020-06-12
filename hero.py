import pygame
import const as c
from init import *


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.hero_type = c.HERO_TYPE            #персонаж, которого выбрал игрок
        self.state = "STAND"                    #текущее состояние героя
        self.facing_right = True                #куда смотрит
     
        self.allow_jump = True
        
        self.frame_index = 0

        self.load_images()
        self.set_physics()
        
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


    def set_physics(self):
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY


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
        self.x_vel = 0
        self.y_vel = 0
        

        if keys[pygame.K_d]:
            self.state = "WALK"
            self.facing_right = True

        elif keys[pygame.K_a]:
            self.state = "WALK"
            self.facing_right = False
            
        elif keys[pygame.K_w]:
            self.state = "JUMP"
            self.y_vel = c.JUMP_VEL
            
  

    def walking(self, keys, fire_group):

        if self.frame_index == 0:
            self.frame_index += 1

        else:
            if self.frame_index < 7:
                self.frame_index += 1
            else:
                self.frame_index = 0
                
        if keys[pygame.K_w]:
            print("w")
            if self.allow_jump:
                self.state = "JUMP"
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.JUMP_VEL - .5
                else:
                    self.y_vel = c.JUMP_VEL

        if keys[pygame.K_d]:
            print("d")
            self.facing_right = True
            
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel
            

        elif keys[pygame.K_a]:
            print("a")
            self.facing_right = False
            
            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel
                
        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = "STAND"
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = "STAND"

        #print(self.x_vel, " ", self.y_vel, " ", self.facing_right)
        #print(keys)
            
  
    def jumping(self, keys, fire_group):
        """Called when Mario is in a JUMP state."""
        #self.allow_jump = False
        self.frame_index = 4
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = "FALL"

        if keys[pygame.K_a]:
            self.facing_right = False
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[pygame.K_d]:
            self.facing_right = True
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        #elif keys[pygame.K_w]:
            #if self.x_vel < self.max_x_vel:
                #self.x_vel += self.x_accel

        if not keys[pygame.K_w]:
            self.gravity = c.GRAVITY
            self.state = "FALL"

        
    def falling(self, keys, fire_group):
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys[pygame.K_a]:
            self.facing_right = False
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[pygame.K_d]:
            self.facing_right = True
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        #elif keys[pygame.K_w]:
            #if self.x_vel < self.max_x_vel:
                #self.x_vel += self.x_accel


    def animation(self):
        if self.facing_right:
            img = self.right_frames[self.frame_index]
            self.image.blit(img, (0,0))
        else:
            img = self.left_frames[self.frame_index]
            self.image.blit(img, (0,0))


    def calculate_animation_speed(self):
        pass
    
