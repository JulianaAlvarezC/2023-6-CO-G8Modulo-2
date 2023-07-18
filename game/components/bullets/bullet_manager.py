import pygame


class BulletManager:
    def __init__(self):
        self.bullets = [] #Guarda las balas del player.
        self.enemy_bullets = [] #Guarda las balas del enemigo.
    
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                game.enemy_manager.remove_enemy()
                game.playing = False
                pygame.time.delay(2000)
                break

        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == "player":
                    self.bullets.remove(bullet)
                    game.enemy_manager.remove_enemy(enemy)
                    break

        #for bullet in self.enemy_bullets: #bucle que recorre la lista
            #bullet.update(self.enemy_bullets) #se vaya dibujando las balas del enemigo.
            #if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy": #colision #acceso al player
                #self.enemy_bullets.remove(bullet)
                #game.playing = False #porque hubo colision y murió, acabó el juego
                #pygame.time.delay(2000) #pausa (2000 milis)
                #break
                
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