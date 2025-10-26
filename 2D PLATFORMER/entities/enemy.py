# entities/enemy.py
import pygame
from core.settings import ENEMY_COLOR

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, patrol_range=(100, 300)):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2
        self.start_x = pos[0]
        self.min_x, self.max_x = patrol_range
        self.direction = 1

    def patrol(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x < self.min_x or self.rect.x > self.max_x:
            self.direction *= -1

    def update(self, tiles):
        self.patrol()
