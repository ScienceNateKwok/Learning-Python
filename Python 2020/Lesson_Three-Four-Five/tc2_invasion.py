# alien_invasion.py

# visit pygame.org/docs/

import pygame
import sys
from tc2settings import Settings
from tc2scattergun import Scattergun
from tc2bullet import Bullet
from tc2agent import Agent

print("Welcome to TC2 Invasion")

class TC2Invasion:

    """class to manage my game"""

    def __init__(self):

        """initialize attributes for the game"""

        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Typical Colors 2 Invasion")

        self.scattergun = Scattergun(self)
        self.bullets = pygame.sprite.Group()
        self.agents = pygame.sprite.Group()

        self._create_fleet()

        #set background color
        self.bg_color = (170, 170, 170)
 
    #methods
    def run_game(self):

        """start the main loop for this game"""
        while True:

            self._check_events()
            self.scattergun.update()
            self._update_bullets()
            self._update_screen()
    def _update_bullets(self):

        """Update position of bullets and get rid of old bullets."""

        #update bullet posision
        self.bullets.update()

            #get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
       
        
            
    def _check_events(self):

        """Respond to keypresses and mouse events."""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self,event):

        """Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.scattergun.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.scattergun.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):

        """Respond to key releases."""

        if event.key == pygame.K_RIGHT:
            self.scattergun.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.scattergun.moving_left = False
                    
        #move the ship to the right
        self.scattergun.rect.x += 1
        
    def _fire_bullet(self):

        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                
    def _update_screen(self):

        """Update images on the screen, and flip to the new screen."""

        #redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.scattergun.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.agents.draw(self.screen)
            
        #make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_fleet(self):

        """Create a fleet of agents."""

        #make an agent

        agent = Agent(self)
        self.agents.add(agent)


if  __name__ == '__main__':

    ai =TC2Invasion()
    ai.run_game()
