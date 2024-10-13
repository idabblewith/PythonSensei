from .config import *
from .laser import Laser


class Spaceship(pg.sprite.Sprite):
    def __init__(
        self,
        sw,
        sh,
        sprite,
        color,
        laser_sfx,
        offset=0,
    ):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Set the offset
        self.offset = offset
        # Set the screen width and height
        self.sw = sw
        self.sh = sh
        # Load the image of the spaceship
        self.image = sprite
        # Set the colour of the image to be GREEN
        self.image.set_colorkey(color)
        # Get the rectangle of the image and set the position to the middle bottom of the screen
        self.rect = self.image.get_rect(
            midbottom=((self.sw + self.offset) / 2, self.sh)
        )
        # Set the speed of the spaceship
        self.speed = 6
        # Create a group for the lasers
        self.lasers_group = pg.sprite.Group()
        # Set
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300  # reload in ms
        self.laser_sound = laser_sfx

    def get_user_input(self):
        # Get the keys that are pressed
        keys = pg.key.get_pressed()
        # Move the spaceship to the right
        if keys[pg.K_RIGHT]:
            self.rect.x += 6
        # Move the spaceship to the left
        if keys[pg.K_LEFT]:
            self.rect.x -= 6
        # Shoot a laser
        if keys[pg.K_SPACE] and self.laser_ready:
            self.shoot()

    def shoot(self):
        # Set the laser to not ready
        self.laser_ready = False
        # Create a new laser with the position of the spaceship, speed of 5 and screen height
        laser = Laser(self.rect.center, 5, self.sh)
        # Add the laser to the lasers group
        self.lasers_group.add(laser)
        # Set the time of the laser
        self.laser_time = pg.time.get_ticks()
        # Play the laser sound
        self.laser_sound.play()

    def constrain_movement(self):
        # Constrain the spaceship to the screen
        if self.rect.right > self.sw:
            self.rect.right = self.sw
        if self.rect.left < self.offset:
            self.rect.left = self.offset

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pg.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def reset(self):
        # Reset the position of the spaceship
        self.rect = self.image.get_rect(
            midbottom=((self.sw + self.offset) / 2, self.sh)
        )
        self.lasers_group.empty()

    def update(self):
        # Get the user input
        self.get_user_input()
        # Constrain the movement of the spaceship
        self.constrain_movement()
        # Update the lasers
        self.lasers_group.update()
        # Recharge the laser
        self.recharge_laser()
