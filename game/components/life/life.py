#import pygame

#from game.utils.constants import LIFE_HEART

#class Life:
    #HEART_WIDTH = 30
    #HEART_HEIGHT= 30
    
    #def __init__(self, total_lives):
        #self.image = LIFE_HEART
        #self.image = pygame.transform.scale(self.image,(self.HEART_WIDTH,self.HEART_HEIGHT))
        #self.rect = self.image.get_rect(topleft=(10, 10))
        #self.total_lives = total_lives
        #self.remaining_lives = total_lives
        #self.is_player_dead = False
    
    #def update(self, game, bullet_manager):
        #if game.playing and bullet_manager.check_player_collision(game.player.rect):
            #self.decrease_life()

    #def draw(self, screen):
        #heart_x = 10
        #for _ in range(self.remaining_lives):
            #screen.blit(self.image, (heart_x, 10))
            #heart_x += self.HEART_WIDTH + 10
        #for _ in range(self.remaining_lives):
            #screen.blit(self.image, self.rect)
            #self.rect.x += 40
        #self.rect.x = 10 
    
    #def decrease_life(self):
        #self.remaining_lives -= 1

    #def is_game_over(self):
        #return self.remaining_lives == 0
        
    #def reset(self):
        #self.remaining_lives = self.total_lives
        #self.is_player_dead = False
 
