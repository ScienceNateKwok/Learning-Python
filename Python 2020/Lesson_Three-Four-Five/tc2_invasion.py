# alien_invasion.py

# visit pygame.org/docs/

import pygame
import sys
from tc2settings import Settings
from tc2scattergun import Scattergun

print("Welcome to TC2 Invasion")

class TC2Invasion:

    """class to manage my game"""

    def __init__(self):

        """initialize attributes for the game"""

        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Typical Colors 2 Invasion")

        self.scattergun = Scattergun(self)

        #set background color
        self.bg_color = (170, 170, 170)
 
    #methods
    def run_game(self):

        """start the main loop for this game"""
        while True:

            self._check_events()
            self.scattergun.update()
            self._update_screen()
    def _check_events(self):

        """Respond to keypresses and mouse events."""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.scattergun.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.scattergun.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.scattergun.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.scattergun.moving_left = False
                    
                    #move the ship to the right
                self.scattergun.rect.x += 1
                
    def _update_screen(self):

        """Update images on the screen, and flip to the new screen."""

        #redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.scattergun.blitme()
        #make the most recently drawn screen visible.
        pygame.display.flip()






if  __name__ == '__main__':

    ai =TC2Invasion()
    ai.run_game()
