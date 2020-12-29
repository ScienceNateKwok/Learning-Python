import pygame

class Scattergun:

    """A class to manage the scattergun"""

    def __init__(self, ai_game):
        """Initialize the scattergun and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the scattergun image and get its rect.
        self.image = pygame.image.load('images/shotgun.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):

        """Update the scattergun's position based on movement flags."""
        #update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.scattergun_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.scattergun_speed

       #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):

        """Draw the scattergun at its current location."""

        self.screen.blit(self.image, self.rect)
