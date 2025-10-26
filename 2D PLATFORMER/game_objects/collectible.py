# objects/collectible.py
import pygame
from core.settings import CRYSTAL_COLOR

class Collectible(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(CRYSTAL_COLOR)
        self.rect = self.image.get_rect(center=pos)
        self.collected = False

    def collect(self, player):
        if self.rect.colliderect(player.rect) and not self.collected:
            self.collected = True
            return True
        return False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)
