import pygame
import main
import const as c
import main

class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hero_type = c.HERO_TYPE            #персонаж, которого выбрал игрок
        self.state = "STAND"                    #текущее состояние героя
        self.facing_right = True                #куда смотрит
        self.allow_jump = True
        self.allow_hit = True
        self.frame_index = 0
        self.walking_timer = 0
        self.last_hit_time = 0 

        self.x_vel = 0                          #forces
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY
        
        self.load_images()

        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)



    def load_images():
        self.left_walking = []
        self.right_walking = []

        self.left_fighting = []
        self.right_fighting = []

        right_walking.append(main.IMAGES["walk0"])
        right_walking.append(main.IMAGES["walk1"])
        right_walking.append(main.IMAGES["walk2"])

        right_fighting.append(main.IMAGES["hit0"])
        right_fighting.append(main.IMAGES["hit1"])

        for image in self.right_walking:
            new_image = pg.transform.flip(image, True, False)
            self.left_walking.append(new_image)

        for image in self.right_fighting:
            new_image = pg.transform.flip(image, True, False)
            self.left_fighting.append(new_image)

        self.walking = [left_walking, right_walking]
        self.fighting = [left_fighting, right_fighting]

        self.right_frames = self.walking[1]
        self.left_frames = self.walking[0]

        self.all_images = [walking, fighting]


    def update(self, keys, game_info, fire_group):
        self.current_time = pygame.time.get_ticks()
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
    
        self.check_to_allow_jump(keys)
        self.check_to_allow_hit(keys)
        
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys['K_SPACE']:                             #hit
            if self.allow_hit:
                self.shoot_fireball(fire_group)

        if keys['K_d']:                                 #walk left
            self.facing_right = False
            self.state = "WALK"
            
        elif keys['K_a']:                               #walk right
            self.facing_right = True
            self.state = "WALK"
            
        elif keys['K_w']:
            if self.allow_jump:
                #setup.SFX['jump'].play()
                self.state = "JUMP"
                self.y_vel = c.JUMP_VEL
        else:
            self.state = "STAND"


    def check_to_allow_jump(self, keys):
        if not keys['K_a']:
            self.allow_jump = True


    def check_to_allow_hit(self, keys):
        if not keys['K_SPACE']:
            self.allow_hit = True


    def walking(self, keys, fire_group):

        self.check_to_allow_jump(keys)
        self.check_to_allow_hit(keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer > self.calculate_animation_speed()):
                if self.frame_index < 2:
                    self.frame_index += 1
                else:
                    self.frame_index = 0

                self.walking_timer = self.current_time

        if keys['K_SPACE']:
            self.max_x_vel = c.MAX_RUN_SPEED
            self.x_accel = c.RUN_ACCEL
            if self.allow_hit:
                self.shoot_fireball(fire_group)
        else:
            self.max_x_vel = c.MAX_WALK_SPEED
            self.x_accel = c.WALK_ACCEL

        if keys['K_w']:                     #jump
            if self.allow_jump:
                #setup.SFX['jump'].play()
                self.state = "JUMP"
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.JUMP_VEL - .5
                else:
                    self.y_vel = c.JUMP_VEL


        if keys['K_a']: #left

            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys['K_d']:
    
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

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


    def shoot_fireball(self, powerup_group):
    
        #setup.SFX['fireball'].play()
        self.fireball_count = self.count_number_of_fireballs(powerup_group)

        if (self.current_time - self.last_hit_time) > 200:
            if self.fireball_count < 2:
                self.allow_hit = False
                #powerup_group.add(powerups.FireBall(self.rect.right, self.rect.y, self.facing_right))
                self.last_hit_time = self.current_time

                self.frame_index = 6
                if self.facing_right:
                    self.image = self.right_fighting[0]
                else:
                    self.image = self.left_left_fighting[0]



    def jumping(self, keys, fire_group):
      
        self.allow_jump = False
        self.frame_index = 4
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity
        self.check_to_allow_hit(keys)

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys['K_a']:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys['K_d']:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not keys['K_a']:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys['K_SPACE']:
            if self.allow_hit:
                self.shoot_fireball(fire_group)



    def falling(self, keys, fire_group):

        self.check_to_allow_hit(keys)
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys['K_a']:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys['K_d']:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if keys['K_SPACE']:
            if self.allow_hit:
                self.shoot_hit(fire_group)


    def animation(self):
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]

     def calculate_animation_speed(self):
         
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed
    
