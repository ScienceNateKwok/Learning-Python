import pygame
from pygame.sprite import Sprite

class Agent(Sprite):

    """A class to represent a single agent in the server."""

    def __init__(self, ai_game):

        """Initialize the agent and set its starting poisition."""

        super().__init__()
        self.screen = ai_game.screen

        #load the alien image and set its rect attribute

        self.image = pygame.image.load('images/agent.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of screen
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position

        self.x = float(self.rect.x)
