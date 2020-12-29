class Settings:

    """A class to store all settings for TC2 Invasion."""

    def __init__(self):

        """Initialize the game's settings."""

        #screen settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (170, 170, 170)

        #scattergun settings
        self.scattergun_speed = 3

        #bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 6
        self.bullet_height = 50
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 2
