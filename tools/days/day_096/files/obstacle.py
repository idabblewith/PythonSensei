from .config import *


class Block(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))


class Obstacle:
    def __init__(self, x, y, block_size, obstacle_grid, color):
        # Pre-create the block image to avoid redundancy
        block_image = pg.Surface((block_size, block_size))
        block_image.fill(color)

        self.blocks_group = pg.sprite.Group()
        for row_index, row in enumerate(obstacle_grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    pos_x = x + col_index * block_size
                    pos_y = y + row_index * block_size
                    block = Block(pos_x, pos_y, block_image)
                    self.blocks_group.add(block)

    def draw(self, screen):
        self.blocks_group.draw(screen)
