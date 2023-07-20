import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
#from game.components.life.life import Life
from game.components.menu import Menu
#from game.components.life.life import Life

from game.components.spaceship import Spaceship
from game.utils.constants import BACKGROUND_MUSIC, BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

class Game:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    def __init__(self):
        pygame.init()
        pygame.mixer.init() #musica.
        pygame.mixer.music.load(BACKGROUND_MUSIC) #Carga un archivo de música para reproducirlo
        pygame.mixer.music.play(-1) #Reproduce la musica en bucle.
        pygame.mixer.music.set_volume(0.2)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False #Esta corriendo el juego pero no jugando.
        self.game_speed = 10 #Control de movimiento. 
        self.x_pos_bg = 0 #blit
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.death_score = 0
        self.score = 0
        #self.player_death = True
        self.menu = Menu("Press any key to start", self.screen) #actualiza el msj.
        
        #self.total_lives = 3
        #self.life = Life(self.total_lives)
        #self.life = Life(total_lives=3)
    
    def execute(self): #ejecutará el juego
        self.running = True #El juego esta corriendo
        while self.running:
            if not self.playing:
                self.show_menu()
            self.events()
            self.update()
            self.draw()
        
        pygame.display.quit()
        pygame.quit()
        
    def run(self):
        # Game loop: events - update - draw
        self.playing = True #Banderita del bucle
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.display.quit()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #La x de la ventana.
                self.playing = False #Finaliza el bucle. 

    def update(self):
        user_input = pygame.key.get_pressed() #Que tecla a presionado.
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        #self.life.update(self, self.bullet_manager)
        #self.life.update(self)

    def draw(self):
        self.clock.tick(FPS) #Unidad de tiempo del juego. #Las contantes van en Mayus.
        self.screen.fill((255, 255, 255)) #Relleno de la pantalla. #Cod. LGB. #255: Blanco
        self.draw_background() #Dibujar el fondo.
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score() ##########
        #self.life.draw(self.screen)
        #self.life.draw(self.screen)
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
        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2 - 20
        half_screen_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_score > 0:
            self.menu.update_message("Death count:" + str(self.death_score) + " Score:"+ str(self.score))
        icon = pygame.transform.scale(ICON, (50, 50))
        self.screen.blit(icon,(half_screen_width, half_screen_height))
        self.menu.draw(self.screen)
        self.menu.update(self)
    
    def update_score(self):
        self.score += 1
        
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)
        
    #def show_death_screen(self):
        #self.draw_score(self.death_score, self.score)
        #pygame.display.update()
        #pygame.time.delay(5000)  # Muestra la pantalla de muerte durante 5 segundos.
        #self.menu.update_message("Perdiste :(")
        #icon = pygame.transform.scale(ICON, (80, 120))
        #self.screen.blit(icon, (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT))
        #self.menu.draw(self.screen)
        #self.menu.update(self, self.death_score)
        
        
    
