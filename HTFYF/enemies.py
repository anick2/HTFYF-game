import pygame
import const as c
import init


class Enemy(pygame.sprite.Sprite):
    """Enemy class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def setup_enemy(self, x, y, direction, name, setup_frames, state):
        """Sets up various values for enemy"""
        self.right_frames = []
        self.right_frames = []
        self.frame_index = 0
        self.death_timer = 0
        self.state = state
        self.flag = False
        self.name = name
        self.direction = direction
        setup_frames()
        self.image = pygame.Surface(c.HERO_SIZE).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def update(self, game_info, *args):
        """Updates enemy behavior"""
        self.handle_state()
        self.animation()

    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == "WALK" or self.state == "HIT_WALK":
            self.walking()

        elif self.state == "FALL":
            self.falling()

    def walking(self):
        """Default state of moving sideways"""
        if self.name == 'mushroom':
            max_frames_hit = 3
            max_frames_walk = 8
        elif self.name == 'spider':
            max_frames_walk = 3

        if self.state == "HIT_WALK":
            if not self.flag:
                self.frame_index = 0
                self.flag = True
            self.right_frames = self.right_fighting
            self.left_frames = self.left_fighting

            if self.frame_index < max_frames_hit:
                self.frame_index += 1

            if self.frame_index == max_frames_hit:
                self.state = "WALK"

        elif self.state == "WALK":
            if self.flag:
                self.frame_index = 0
                self.flag = False
            self.right_frames = self.right_walking
            self.left_frames = self.left_walking

            if self.frame_index == 0:
                self.frame_index += 1

            else:
                if self.frame_index < max_frames_walk:
                    self.frame_index += 1
                else:
                    self.frame_index = 0

    def falling(self):
        pass

    def animation(self):
        """Basic animation, switching between two frames"""
        if self.direction == 'right':
            img = self.right_frames[self.frame_index]
            self.image.blit(img, (0, 0))
        else:
            img = self.left_frames[self.frame_index]
            self.image.blit(img, (0, 0))


class Mushroom(Enemy):
    """Mushroom class"""
    def __init__(self, x=300, y=c.HEIGHT - c.HEIGHT_OF_GROUND,
                 direction='left', name='mushroom', state='WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 1
        self.y_vel = 0

    def setup_frames(self):
        self.frame_index = 0

        self.left_walking = []
        self.right_walking = []

        self.left_fighting = []
        self.right_fighting = []

        for i in range(1, 10):
            img = pygame.transform.scale(init.IMAGES["m_walk_"
                                         + str(i)], c.HERO_SIZE)
            self.left_walking.append(img)
        for i in range(1, 5):
            img = pygame.transform.scale(init.IMAGES["m_hit_"
                                         + str(i)], c.HERO_SIZE)
            self.left_fighting.append(img)

        for image in self.left_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.right_walking.append(new_image)

        for image in self.left_fighting:
            new_image = pygame.transform.flip(image, True, False)
            self.right_fighting.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking


class Spider(Enemy):
    """Spider class"""
    def __init__(self, x=300, y=c.HEIGHT - c.HEIGHT_OF_GROUND,
                 direction='left', name='spider', state='WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 2
        self.y_vel = 0

    def setup_frames(self):
        self.frame_index = 0

        self.left_walking = []
        self.right_walking = []

        for i in range(1, 5):
            img = pygame.transform.scale(init.IMAGES["s_walk_"
                                         + str(i)], c.HERO_SIZE)
            self.left_walking.append(img)

        for image in self.left_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.right_walking.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking


class Cop(Enemy):
    """Cop class"""
    def __init__(self, x=300, y=c.HEIGHT - c.HEIGHT_OF_GROUND,
                 direction='left', name='spider', state='WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 3
        self.y_vel = 0

    def setup_frames(self):
        self.frame_index = 0
        self.left_walking = []
        self.right_walking = []

        for i in range(1, 5):
            img = pygame.transform.scale(init.IMAGES["r_walk_"
                                         + str(i)], c.HERO_SIZE)
            self.left_walking.append(img)

        for image in self.left_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.right_walking.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking


class Granny(Enemy):
    """Granny class"""
    def __init__(self, x=300, y=c.HEIGHT - c.HEIGHT_OF_GROUND,
                 direction='left', name='spider', state='WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 2
        self.y_vel = 0

    def setup_frames(self):
        self.frame_index = 0
        self.left_walking = []
        self.right_walking = []

        for i in range(1, 5):
            img = pygame.transform.scale(init.IMAGES["b_walk_"
                                         + str(i)], c.HERO_SIZE)
            self.left_walking.append(img)

        for image in self.left_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.right_walking.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking


class Bear(Enemy):
    """Bear class"""
    def __init__(self, x=300, y=c.HEIGHT - c.HEIGHT_OF_GROUND,
                 direction='left', name='spider', state='WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 2
        self.y_vel = 0

    def setup_frames(self):
        self.frame_index = 0

        self.left_walking = []
        self.right_walking = []

        for i in range(1, 5):
            img = pygame.transform.scale(init.IMAGES["a_walk_"
                                         + str(i)], c.HERO_SIZE)
            self.left_walking.append(img)

        for image in self.left_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.right_walking.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking


class Clown(Enemy):
    """Clown class"""
    def __init__(self, x=300, y=c.HEIGHT - c.HEIGHT_OF_GROUND,
                 direction='left', name='spider', state='WALK'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames, state)
        self.x_vel = 1
        self.y_vel = 0

    def setup_frames(self):
        self.frame_index = 0

        self.left_walking = []
        self.right_walking = []

        for i in range(1, 5):
            img = pygame.transform.scale(init.IMAGES["c_walk_"
                                         + str(i)], c.HERO_SIZE)
            self.left_walking.append(img)

        for image in self.left_walking:
            new_image = pygame.transform.flip(image, True, False)
            self.right_walking.append(new_image)

        self.right_frames = self.right_walking
        self.left_frames = self.left_walking
