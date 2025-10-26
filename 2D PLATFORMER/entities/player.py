# entities/player.py
import pygame
from core.settings import PLAYER_COLOR

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 48))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_force = 10
        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel.x = 0
        if keys[pygame.K_LEFT]:
            self.vel.x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.vel.x = self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel.y = -self.jump_force

    def apply_gravity(self):
        self.vel.y += 0.5
        if self.vel.y > 10:
            self.vel.y = 10

    def move_and_collide(self, tiles):
        self.rect.x += self.vel.x
        self.check_collision(tiles, 'x')

        self.rect.y += self.vel.y
        self.check_collision(tiles, 'y')

    def check_collision(self, tiles, direction):
        self.on_ground = False
        for tile in tiles:
            if self.rect.colliderect(tile):
                if direction == 'x':
                    if self.vel.x > 0:
                        self.rect.right = tile.left
                    elif self.vel.x < 0:
                        self.rect.left = tile.right
                elif direction == 'y':
                    if self.vel.y > 0:
                        self.rect.bottom = tile.top
                        self.on_ground = True
                        self.vel.y = 0
                    elif self.vel.y < 0:
                        self.rect.top = tile.bottom
                        self.vel.y = 0

    def update(self, tiles):
        self.handle_input()
        self.apply_gravity()
        self.move_and_collide(tiles)
