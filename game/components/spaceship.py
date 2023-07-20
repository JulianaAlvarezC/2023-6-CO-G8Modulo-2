from pygame.sprite import Sprite
import pygame
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.utils.constants import SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH, SHOOT_SOUND

class Spaceship(Sprite): #clase padre, como img.
    SHIP_WIDTH = 40 #Ancho de la nave.
    SHIP_HEIGHT = 60 #Alto de la nave.
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH #Posicion incial de la nave. En x
    Y_POS = 500
    SHIP_SPEED = 10
    def __init__(self):
        self.image = SPACESHIP #Img de la nave.
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH,self.SHIP_HEIGHT)) #Tamaño de la nave.
        self.rect = self.image.get_rect() #Alto y ancho (posiciones)
        self.rect.x = self.X_POS #Posicion incial de la nave. En x
        self.rect.y = self.Y_POS
        self.type = "player"
        self.bullet_manager = BulletManager()
        self.shooting_delay = 0  # Variable para controlar el tiempo entre disparos
        self.shooting_cooldown = 0
        self.is_shooting = False
        #self.player_dead = False ######
        
    def update(self, user_input, game): #Teclas que se están usando para cambiar la posicion.
        if user_input[pygame.K_LEFT]: #Con el if, se combinan las teclas.
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE] and not self.is_shooting:  #Verificar si se presiona la tecla ESPACIO y no se está disparando actualmente
            self.shoot(game.bullet_manager)
            self.is_shooting = True  #Establece la banderita de disparo a True
        if not user_input[pygame.K_SPACE]:  #Verifica si se suelta la tecla ESPACIO
            self.is_shooting = False 
    
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y)) #dibujar las imagenes y las posiciones.
        
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH 
    
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = self.rect.width
    
    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
        if self.rect.y < 0:
            self.rect.y = 0
            #pygame.mixer.Sound(BOUNDARY_SOUND).play()
            #self.enemy_appear_sound.set_volume(0.5) 
    
    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        if self.rect.y + self.SHIP_HEIGHT > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.SHIP_HEIGHT
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
        if current_time - self.shooting_delay > self.shooting_cooldown:  # Verificar si ha pasado suficiente tiempo para disparar
            bullet = Bullet(self)  
            bullet_manager.add_bullet(bullet)  # Agrega la bala al BulletManager
            pygame.mixer.Sound(SHOOT_SOUND).play()
            self.shooting_delay = current_time 
    
    #def reset_player(self):
        #self.player.rect.x = Spaceship.X_POS
        #self.player.rect.y = Spaceship.Y_POS
    

        
    
