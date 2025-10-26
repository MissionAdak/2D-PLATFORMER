# levels/level_manager.py
from levels.level_1 import create_level
from entities.enemy import Enemy
from game_objects.collectible import Collectible


class LevelManager:
    def __init__(self):
        # Start with level 1
        self.current_level = 1
        self.tiles = create_level()
        self.enemies = [Enemy((400, 400), (380, 500))]
        self.crystals = [Collectible((680, 210))]


    def update(self, player):
        # Check enemy collisions
        for enemy in self.enemies:
            if player.rect.colliderect(enemy.rect):
                player.rect.topleft = (100, 100)  # respawn
                player.vel = player.vel * 0

        # Check crystal collection
        for crystal in self.crystals:
            crystal.collect(player)

    def draw(self, screen):
        for crystal in self.crystals:
            crystal.draw(screen)

