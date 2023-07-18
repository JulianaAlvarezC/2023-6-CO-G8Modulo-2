import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600 #Alto de la pantalla
SCREEN_WIDTH = 1100 #Ancho de la pantalla
FPS = 30 #Velocidad.
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP_J = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/ShipJ.png"))
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'

# Sound Constants
SOUND_DIR = os.path.join("game", "sounds")

BACKGROUND_MUSIC = os.path.join(SOUND_DIR, "background_sound.wav")
SHOOT_SOUND = os.path.join(SOUND_DIR, "laser_shot.wav")
ENEMY_APPEAR_SOUND = os.path.join(SOUND_DIR, "appearance.wav")
BOUNDARY_SOUND = os.path.join(SOUND_DIR, "boundary.wav")
#APPEARANCE_SOUND = os.path.join(SOUND_DIR, "appearance.wav")