import pygame
import const as c
import init


class Hero(pygame.sprite.Sprite):
    """Hero class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = "STAND"
        self.facing_right = True
        self.allow_jump = True
        self.flag = False
        self.frame_index = 0
        self.load_images()
        self.set_physics()
        img = self.right_frames[self.frame_index]
        self.image = pygame.Surface(c.HERO_SIZE).convert()
        self.image.set_colorkey((0, 0, 0))
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
            img = pygame.transform.scale(init.IMAGES["walk"
                                         + str(i) + c.HERO_TYPE], c.HERO_SIZE)
            self.right_walking.append(img)

        for i in range(1, 8):
            img = pygame.transform.scale(init.IMAGES["hit"
                                         + str(i) + c.HERO_TYPE], c.HERO_SIZE)
            self.right_fighting.append(img)

        for image in self.right_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.left_walking.append(new_image)

        for image in self.right_fighting:
            new_image = pygame.transform.flip(image, True, False)
            self.left_fighting.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking

    def set_physics(self):
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY

    def update(self, keys, fire_group):
        """Updates Hero states and animations once per frame"""
        self.handle_state(keys, fire_group)
        self.animation()

    def handle_state(self, keys, fire_group):
        """Determines Hero's behavior based on his state"""
        if keys[pygame.K_SPACE]:
            if self.state == "JUMP":
                self.state = "HIT_FALL"
            elif self.state == "FALL":
                self.state = "HIT_FALL"

        if (self.state == "STAND") or (self.state == "HIT_STAND"):
            self.standing(keys, fire_group)

        elif (self.state == "WALK") or (self.state == "HIT_WALK"):
            self.walking(keys, fire_group)

        elif (self.state == "JUMP") or (self.state == "HIT_JUMP"):
            self.jumping(keys, fire_group)

        elif (self.state == "FALL") or (self.state == "HIT_FALL"):
            self.falling(keys, fire_group)

    def standing(self, keys, fire_group):
        """This function is called if Mario is standing still"""
        self.x_vel = 0
        self.y_vel = 0

        if not keys[pygame.K_w]:
            self.allow_jump = True

        if (self.state == "HIT_STAND"):
            if not self.flag:
                self.frame_index = 0
                self.flag = True
            max_frames = 5
            self.right_frames = self.right_fighting
            self.left_frames = self.left_fighting

            if self.frame_index < max_frames:
                self.frame_index += 1

            if self.frame_index == max_frames:
                self.state = "STAND"

        elif (self.state == "STAND"):
            if self.flag:
                self.frame_index = 0
                self.flag = False
            self.right_frames = self.right_walking
            self.left_frames = self.left_walking

        if keys[pygame.K_SPACE]:
            self.state = "HIT_STAND"

        if keys[pygame.K_d]:
            self.state = "WALK"
            self.facing_right = True

        elif keys[pygame.K_a]:
            self.state = "WALK"
            self.facing_right = False

        elif keys[pygame.K_w] and self.allow_jump:
            self.state = "JUMP"
            self.y_vel = c.JUMP_VEL

    def walking(self, keys, fire_group):
        """This function is called when Hero is in a walking state"""
        if not keys[pygame.K_w]:
            self.allow_jump = True

        if (self.state == "HIT_WALK"):
            if not self.flag:
                self.frame_index = 0
                self.flag = True
            max_frames = 5
            self.right_frames = self.right_fighting
            self.left_frames = self.left_fighting

            if self.frame_index < max_frames:
                self.frame_index += 1

            if self.frame_index == max_frames:
                self.state = "WALK"

        elif (self.state == "WALK"):
            if self.flag:
                self.frame_index = 0
                self.flag = False
            max_frames = 7
            self.right_frames = self.right_walking
            self.left_frames = self.left_walking

            if self.frame_index == 0:
                self.frame_index += 1

            else:
                if self.frame_index < max_frames:
                    self.frame_index += 1
                else:
                    self.frame_index = 0

        if keys[pygame.K_SPACE]:
            self.state = "HIT_WALK"

        if keys[pygame.K_w]:
            if self.allow_jump:
                self.state = "JUMP"
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.JUMP_VEL - .5
                else:
                    self.y_vel = c.JUMP_VEL

        if keys[pygame.K_d]:
            self.facing_right = True
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        elif keys[pygame.K_a]:
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
                    self.x_vel -= 3 * self.x_accel
                else:
                    self.x_vel = 0
                    self.state = "STAND"
            else:
                if self.x_vel < 0:
                    self.x_vel += 3 * self.x_accel
                else:
                    self.x_vel = 0
                    self.state = "STAND"

    def jumping(self, keys, fire_group):
        """This function is called when Hero is in a jumping state"""
        self.allow_jump = False
        if (self.state == "HIT_JUMP"):
            if not self.flag:
                self.frame_index = 0
                self.flag = True
            max_frames = 5
            self.right_frames = self.right_fighting
            self.left_frames = self.left_fighting

            if self.frame_index < max_frames:
                self.frame_index += 1

            if self.frame_index == max_frames:
                self.state = "JUMP"

        elif (self.state == "JUMP"):
            if self.flag:
                self.frame_index = 0
                self.flag = False

        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity

        if keys[pygame.K_SPACE]:
            self.state = "HIT_JUMP"

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = "FALL"

        if keys[pygame.K_a]:
            self.facing_right = False

            if self.x_vel > (self.max_x_vel * -1):
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
        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= 3 * self.x_accel
                else:
                    self.x_vel = 0
            else:
                if self.x_vel < 0:
                    self.x_vel += 3 * self.x_accel
                else:
                    self.x_vel = 0

        if not keys[pygame.K_w]:
            self.gravity = c.GRAVITY
            self.state = "FALL"
            if self.flag:
                self.state = "HIT_FALL"

    def falling(self, keys, fire_group):
        """This function is called when Hero is in a falling state"""
        if (self.state == "HIT_FALL"):
            if not self.flag:
                self.frame_index = 0
                self.flag = True
            max_frames = 5
            self.right_frames = self.right_fighting
            self.left_frames = self.left_fighting

            if self.frame_index < max_frames:
                self.frame_index += 1

            if self.frame_index == max_frames:
                self.state = "FALL"
        else:
            if self.flag:
                self.frame_index = 0
                self.flag = False

        if keys[pygame.K_SPACE]:
            self.state = "HIT_FALL"

        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys[pygame.K_a]:
            self.facing_right = False

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel / 2
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[pygame.K_d]:
            self.facing_right = True

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel / 2
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

    def animation(self):
        """Hero's image for animation"""
        if self.facing_right:
            img = self.right_frames[self.frame_index]
            self.image.blit(img, (0, 0))
        else:
            img = self.left_frames[self.frame_index]
            self.image.blit(img, (0, 0))
