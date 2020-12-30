# alien_invasion.py

# visit pygame.org/docs/

import pygame
import sys
from tc2settings import Settings
from tc2scattergun import Scattergun
from tc2bullet import Bullet
from tc2agent import Agent

print("Welcome to TC2 Invasion. Press 'esc' to quit.")

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousebutton_events(event)
                
    def _check_keydown_events(self,event):

        """Respond to keypresses. """

        LEFT = 1

        if event.key == pygame.K_d:
            self.scattergun.moving_right = True
        elif event.key == pygame.K_a:
            self.scattergun.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
            
    def _check_keyup_events(self, event):

        """Respond to key releases."""

        if event.key == pygame.K_d:
            self.scattergun.moving_right = False
        elif event.key == pygame.K_a:
            self.scattergun.moving_left = False
                    
        #move the ship to the right
        self.scattergun.rect.x += 1
        
    def _check_mousebutton_events(self,event):

        """Respond to mouse click. """


        if event.button == 1:
            self._fire_bullet()
        
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

        #create an agent and find the number of agents in a row

        #spacing between each alien is equal to one alien width

        agent = Agent(self)
        agent_width, agent_height = agent.rect.size
        available_space_x = self.settings.screen_width - (2 * agent_width)
        number_agents_x = available_space_x // (2 * agent_width)

        #determine the number of rows of aliens that fit on the screen.
        scattergun_height = self.scattergun.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * agent_height) - scattergun_height)
        number_rows = available_space_y // (2 * agent_height)

        #create the full fleet of agents
        
        for row_number in range(number_rows):
            for agent_number in range(number_agents_x):
                self._create_agent(agent_number, row_number)
    

    def _create_agent(self, agent_number, row_number):
            
        #create an agent and place it in the row
        agent = Agent(self)
        agent_width, agent_height = agent.rect.size
        agent.x = agent_width + 2 * agent_width * agent_number
        agent.rect.x = agent.x
        agent.rect.y = agent.rect.height + 2 * agent.rect.height * row_number
        self.agents.add(agent)

        
        

        


if  __name__ == '__main__':

    ai =TC2Invasion()
    ai.run_game()
