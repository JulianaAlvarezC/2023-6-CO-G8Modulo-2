import pygame


class BulletManager:
    def __init__(self):
        self.bullets = [] #Guarda las balas del player.
        self.enemy_bullets = [] #Guarda las balas del enemigo.
    
    def update(self, game):
        player_dead = False 
        
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                game.playing = False
                game.death_score += 1 
                game.player.player_dead = True 
                pygame.time.delay(2000)
                

        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == "player":
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score += 100
                    
        if not game.playing:
            game.player.player_dead = False
                
    def draw(self, screen):
        for bullet in self.enemy_bullets:#recorrer 
            bullet.draw(screen)
            
        for bullet in self.bullets: # Dibujar las balas del jugador.
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len (self.enemy_bullets) < 1:  #cada enemigo dispare una bala y la longitud de la lista es menor a 1, le agg
            self.enemy_bullets.append(bullet) #entonces le agg balas
        elif bullet.owner == "player":
            self.bullets.append(bullet)
    
    #def check_player_collision(self, player_rect):
        #for bullet in self.enemy_bullets:
            #if bullet.rect.colliderect(player_rect) and bullet.owner == "enemy":
                #return True
        #return False