import pygame as pg
import os, sys, random

from days.day_096.files.laser import Laser

from .alien import Alien, MysteryShip
from .obstacle import Obstacle
from .spaceship import Spaceship

# Colours
GREEN = (34, 255, 76)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (243, 216, 63)

# Path Constants
BASE_DIR = os.path.dirname(__file__)
SPRITE_PATH = os.path.join(BASE_DIR, "sprites")
FONT_PATH = os.path.join(BASE_DIR, "fonts")
SFX_PATH = os.path.join(BASE_DIR, "sfx")
BGM_PATH = os.path.join(BASE_DIR, "bgm")

pg.font.init()  # Initialize the font module
pg.mixer.init()  # Initialize the mixer module
pg.mixer.music.set_volume(0.2)

FONT = pg.font.Font(os.path.join(FONT_PATH, "monogram.ttf"), 40)
LEVEL_UI = FONT.render("LEVEL 01", False, YELLOW)
GG_UI = FONT.render("GAME OVER", False, YELLOW)
SCORE_UI = FONT.render("SCORE", False, YELLOW)
HIGHSCORE_UI = FONT.render("HIGH-SCORE", False, YELLOW)


MYSTERY_SHIP_SPEED = 3
OFFSET = 50

# Preload Sprites
ALIEN_TYPES = ["1", "2", "3"]  # Example alien types
ALIEN_IMAGES = {
    type_: pg.image.load(os.path.join(SPRITE_PATH, f"alien_{type_}.png"))
    for type_ in ALIEN_TYPES
}
SHIP_IMG = pg.image.load(os.path.join(SPRITE_PATH, "spaceship.png"))
MYSTERY_IMG = pg.image.load(os.path.join(SPRITE_PATH, "mystery.png"))


# Preload Sounds
LASER_SFX = pg.mixer.Sound(
    os.path.join(
        SFX_PATH,
        "laser.ogg",
    )
)
LASER_SFX.set_volume(0.2)

EXPLOSION_SFX = pg.mixer.Sound(
    os.path.join(
        SFX_PATH,
        "explosion.ogg",
    )
)
EXPLOSION_SFX.set_volume(0.2)

MUSIC = pg.mixer.music.load(os.path.join(BGM_PATH, "music.ogg"))


# Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
FPS = 60
BLOCK_SIZE = 3


OBSTACLE_GRID = [
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
]


# Create a Game class that will handle the logic
class GameLogic:
    def __init__(self, sw, sh, offset):
        self.screen_width = sw
        self.screen_height = sh
        self.offset = offset
        self.spaceship_group = pg.sprite.GroupSingle()
        self.spaceship_group.add(
            Spaceship(
                self.screen_width,
                self.screen_height,
                SHIP_IMG,
                GREEN,
                LASER_SFX,
                self.offset,
            )
        )
        self.obstacles = self.create_obstacles()
        self.aliens_group = pg.sprite.Group()
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_lasers_group = pg.sprite.Group()
        self.mystery_ship_group = pg.sprite.GroupSingle()
        self.lives = 3
        self.run = True
        self.score = 0
        self.highscore = 0
        self.explosion_sound = EXPLOSION_SFX
        self.load_highscore()
        pg.mixer.music.play(-1)

    def create_obstacles(self):
        obstacle_width = len(OBSTACLE_GRID[0]) * 3
        gap = (self.screen_width + self.offset - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(
                offset_x,
                self.screen_height - 100,
                BLOCK_SIZE,
                OBSTACLE_GRID,
                GREEN,
            )
            obstacles.append(obstacle)
        return obstacles

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = 75 + column * 55
                y = 110 + row * 55

                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1

                alien = Alien(alien_type, x + self.offset / 2, y, ALIEN_IMAGES)
                self.aliens_group.add(alien)

    def move_aliens(self):
        self.aliens_group.update(self.aliens_direction)

        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width - alien.rect.width / 2:
                self.aliens_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= self.offset / 2:
                self.aliens_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
            self.alien_lasers_group.add(laser_sprite)

    def create_mystery_ship(self):
        self.mystery_ship_group.add(
            MysteryShip(
                self.screen_width,
                self.offset,
                MYSTERY_IMG,
                MYSTERY_SHIP_SPEED,
            )
        )

    def check_for_collisions(self):
        # Spaceship
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:

                aliens_hit = pg.sprite.spritecollide(
                    laser_sprite, self.aliens_group, True
                )
                if aliens_hit:
                    self.explosion_sound.play()
                    for alien in aliens_hit:
                        self.score += alien.type * 100
                        self.check_for_highscore()
                        laser_sprite.kill()

                if pg.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    self.score += 500
                    self.explosion_sound.play()
                    self.check_for_highscore()
                    laser_sprite.kill()

                for obstacle in self.obstacles:
                    if pg.sprite.spritecollide(
                        laser_sprite, obstacle.blocks_group, True
                    ):
                        laser_sprite.kill()

        # Alien Lasers
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pg.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()

                for obstacle in self.obstacles:
                    if pg.sprite.spritecollide(
                        laser_sprite, obstacle.blocks_group, True
                    ):
                        laser_sprite.kill()

        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pg.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pg.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()

    def game_over(self):
        self.run = False

    def reset(self):
        self.run = True
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.create_aliens()
        self.mystery_ship_group.empty()
        self.obstacles = self.create_obstacles()
        self.score = 0

    def check_for_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open(os.path.join(BASE_DIR, "highscore.txt"), "w") as file:
                file.write(str(self.highscore))

    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0
