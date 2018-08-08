import pygame

from .animation import Animation
from .utils import load_img


class Player(pygame.sprite.Sprite):
    animation_speed = 5
    moving_speed = 5

    x_pos = 0
    y_pos = 0

    # 1 right
    # 0 idle
    # -1 left
    direction = 0

    current_animation = None
    animations = {}

    def __init__(self):
        super(Player, self).__init__()
        self._image = load_img('sprites/ghost.png')
        self.rect = pygame.Rect(0, 0, 16, 16)
        self.facing = -1
        self.animations['idle'] = Animation(self._image, 3)
        self.current_animation = self.animations['idle']
        self.image = self.current_animation.frames[self.current_animation.current_frame]

    def update(self, *args):
        self.current_animation.update(self.animation_speed)
        self.image = self.current_animation.frames[self.current_animation.current_frame]

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.direction = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.direction = -1
            else:
                self.direction = 0

        if self.direction:
            self.rect = self.rect.move(self.moving_speed * self.direction, 0)
