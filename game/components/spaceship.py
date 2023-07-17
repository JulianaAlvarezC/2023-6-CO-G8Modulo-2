
from pygame.sprite import Sprite
import pygame

from game.utils.constants import SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH

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
        self.rect.x = (SCREEN_WIDTH // 2) - self.SHIP_WIDTH #Posicion incial de la nave. En x
        self.rect.y = self.SHIP_HEIGHT
    
    def update(self, user_input): #Teclas que se están usando para cambiar la posicion.
        if user_input[pygame.K_LEFT]: #Con el if, se combinan las teclas.
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
    
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
    
    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        if self.rect.y + self.SHIP_HEIGHT > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.SHIP_HEIGHT
    

        
    
