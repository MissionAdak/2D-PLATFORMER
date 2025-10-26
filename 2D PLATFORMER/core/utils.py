# core/utils.py
import pygame

def draw_text(screen, text, pos, color=(255,255,255), size=32):
    font = pygame.font.SysFont(None, size)
    surf = font.render(text, True, color)
    screen.blit(surf, pos)
