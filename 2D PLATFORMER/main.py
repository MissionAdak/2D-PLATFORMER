# main.py
import pygame
from core.settings import *
from core.utils import draw_text
from entities.player import Player
from levels.level_manager import LevelManager

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mission's  Game - Level 1")
clock = pygame.time.Clock()

player = Player((100, 100))
all_sprites = pygame.sprite.Group(player)

level_manager = LevelManager()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update(level_manager.tiles)
    for enemy in level_manager.enemies:
        enemy.update(level_manager.tiles)
    level_manager.update(player)

    # Draw
    screen.fill(BG_COLOR)
    for tile in level_manager.tiles:
        pygame.draw.rect(screen, GROUND_COLOR, tile)
    level_manager.draw(screen)

    for enemy in level_manager.enemies:
        pygame.draw.rect(screen, (255, 80, 80), enemy.rect)

    all_sprites.draw(screen)

    # HUD
    crystals_left = sum(not c.collected for c in level_manager.crystals)
    draw_text(screen, f"Crystals left: {crystals_left}", (10, 10))

    pygame.display.flip()

pygame.quit()

