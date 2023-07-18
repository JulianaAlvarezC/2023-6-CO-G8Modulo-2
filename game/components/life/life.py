import pygame

class Life:
    def __init__(self, total_lives):
        self.total_lives = total_lives
        self.remaining_lives = total_lives
        self.font = pygame.font.SysFont(None, 36)
    
    def update(self, game):
        if pygame.sprite.spritecollide(game.player, game.enemy_manager.enemies, True):
            self.remaining_lives -= 1
            if self.remaining_lives <= 0:
                game.playing = False
                pygame.time.delay(2000)
                # Resto de la lógica para el final del juego
    
    def draw(self, screen):
        text = self.font.render(f"Vidas: {self.remaining_lives}", True, (255, 255, 255))
        screen.blit(text, (10, 10))