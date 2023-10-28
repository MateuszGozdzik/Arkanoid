import pygame
import random

class BlockManager:
    class Block:
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
        def draw_me(self, screen):
            pygame.draw.rect(
                screen, self.color, (self.x, self.y, self.width, self.height)
            )

    def __init__(self) -> None:
        self.block_width, self.block_height = 80, 30
        self.blocks = []
        self.COLORS = {
            # name: [rgb, points, hit's to break]
            "white": [(255, 255, 255), 50, 1],
            "orange": [(255, 165, 0), 60, 1],
            "cyan": [(0, 255, 255), 70, 1],
            "green": [(0, 255, 0), 80, 1],
            "red": [(255, 0, 0), 90, 1],
            "blue": [(0, 0, 255), 100, 1],
            "purple": [(127, 0, 255), 110, 1],
            "yellow": [(255, 255, 0), 120, 1],
        }
        self.COLOR_LIST = [color for color in self.COLORS]


    def add_blocks(self, window_size, num_rows, num_cols):
        color_list_extended = self.COLOR_LIST * ((num_rows * num_cols) // len(self.COLOR_LIST) + 1)
        while len(color_list_extended) != num_cols * num_rows:
            color_list_extended.pop()
        random.shuffle(color_list_extended)
        
        block_width_with_padding = self.block_width + 5
        block_height_with_padding = self.block_height + 5
        
        start_x = (window_size[0] - (num_cols * block_width_with_padding - 5)) // 2
        start_y = (window_size[1] - (num_rows * block_height_with_padding - 5)) // 2 - 50

        self.blocks.extend([
            self.Block(
                x=start_x + col * block_width_with_padding,
                y=start_y + row * block_height_with_padding,
                width=self.block_width,
                height=self.block_height,
                color=color_list_extended.pop()
            )
            for row in range(num_rows)
            for col in range(num_cols)
        ])


    def draw_blocks(self, screen):
        for block in self.blocks:
            block.draw_me(screen)