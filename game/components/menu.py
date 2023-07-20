import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 #Mitad de la pantalla. 
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    
    def __init__(self, message, screen):
        screen.fill((0, 0, 0)) #fondo en color blanco
        self.font = pygame.font.Font(FONT_STYLE, 50) #Fuente (tipo de letra, tamaño)
        self.text = self.font.render(message, True, (0, 0, 0)) #antialias, evitar sombras (true), [color de texto]
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        
    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game) #llamara a todos los eventos que ocurran en el menu y lo manda al juego
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
    
    def handle_events_on_menu(self, game): #esto se ejecuta al principio.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False #Si estoy en el menu y cierro la ventana me voy a salir
                game.running = False
            elif event.type == pygame.KEYDOWN: #controla si se presiona cualquier tecla.
                game.run()
                
    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))
    
    def update_message(self, message): #recibe msjs y lo convierte en img, para mostrarlo en pantalla.
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect() #posicion de la recta
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT) #se pone en el centro.
        
