# levels/level_1.py
import pygame
from core.settings import TILE_SIZE, SCREEN_HEIGHT

def create_level():
    """Return a list of ground and platform tiles as pygame.Rects"""
    tiles = []

    # Ground layer
    for x in range(0, 800, TILE_SIZE):
        tiles.append(pygame.Rect(x, SCREEN_HEIGHT - TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Floating platforms
    tiles.append(pygame.Rect(200, 360, 120, 40))
    tiles.append(pygame.Rect(450, 300, 120, 40))
    tiles.append(pygame.Rect(650, 250, 100, 40))

    return tiles
