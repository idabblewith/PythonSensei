from .config import *


class Laser(pg.sprite.Sprite):
    def __init__(self, pos, speed, sh):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Create a surface for the laser without image (4 by 15 px)
        self.image = pg.Surface((4, 15))
        # Fill the surface with a yellow color
        self.image.fill((243, 216, 63))
        # Get the rectangle of the image and set the position to the center of the spaceship
        self.rect = self.image.get_rect(center=pos)
        # Set the speed of the laser
        self.speed = speed
        # Set the screen height
        self.sh = sh

    def update(self):
        # Move the laser up on each tick
        self.rect.y -= self.speed
        # If the laser is out of the screen, remove it to save memory
        if self.rect.bottom < 0:
            self.kill()
