import pygame
from game.components.enemies.enemy_manager import EnemyManager

from game.components.spaceship import Spaceship
from game.utils.constants import BACKGROUND_MUSIC, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() #musica.
        pygame.mixer.music.load(BACKGROUND_MUSIC) #Carga un archivo de música para reproducirlo
        pygame.mixer.music.play(-1) #Reproduce la musica en bucle.
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 #Control de movimiento. 
        self.x_pos_bg = 0 #blit
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True #Banderita del bucle
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #La x de la ventana.
                self.playing = False #Finaliza el bucle. 

    def update(self):
        user_input = pygame.key.get_pressed() #Que tecla a presionado.
        self.player.update(user_input)
        self.enemy_manager.update()

    def draw(self):
        self.clock.tick(FPS) #Unidad de tiempo del juego. #Las contantes van en Mayus.
        self.screen.fill((255, 255, 255)) #Relleno de la pantalla. #Cod. LGB. #255: Blanco
        self.draw_background() #Dibujar el fondo.
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        pygame.display.flip() #Fija todo lo que se hace con blit.

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) #Dibujo en borrador.
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height)) #Animación.
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height)) #Imegen que se superpone.
            self.y_pos_bg = 0 #Reseteo de la posición en y. 
        self.y_pos_bg += self.game_speed #Control de movimiento. 
