from .config import *


class Alien(pg.sprite.Sprite):
    def __init__(self, type_, x, y, alien_img_array):
        super().__init__()
        self.type = type_
        # Use pre-loaded image from the dictionary
        self.image = alien_img_array[str(self.type)]
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        # Update alien position based on direction
        self.rect.x += direction


class MysteryShip(pg.sprite.Sprite):
    def __init__(self, screen_width, offset, img, speed):
        super().__init__()
        self.screen_width = screen_width
        self.image = img
        self.offset = offset
        self.speed = speed

        # Randomly choose the initial position (left or right side of the screen)
        self.rect = self.image.get_rect(topleft=self._get_initial_position())
        self.speed = self._get_initial_speed()

    def _get_initial_position(self):
        # Choose a starting position based on screen width and offset
        x = random.choice(
            [self.offset // 2, self.screen_width + self.offset - self.image.get_width()]
        )
        return (x, 90)

    def _get_initial_speed(self):
        # Set speed based on starting position (left-to-right or right-to-left)
        if self.rect.left < self.screen_width // 2:
            return self.speed
        else:
            return -self.speed

    def update(self):
        # Update mystery ship position
        self.rect.x += self.speed

        # Remove the sprite if it moves off-screen
        if (
            self.rect.right > self.screen_width + self.offset // 2
            or self.rect.left < self.offset // 2
        ):
            self.kill()
