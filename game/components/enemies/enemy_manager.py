import random

import pygame
from game.utils.constants import ENEMY_APPEAR_SOUND
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_appear_sound = pygame.mixer.Sound(ENEMY_APPEAR_SOUND) 
        self.enemy_appear_sound.set_volume(0.5) 

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1,2)
        if enemy_type == 1:
            enemy = Enemy()
        else: 
            x_speed = 5
            y_speed = 2
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        if len (self.enemies) < 1:
            self.enemies.append(enemy)
            self.enemy_appear_sound.play()
        
