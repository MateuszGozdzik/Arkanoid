import pygame


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

    def add_blocks(self, window_size, num_rows, num_cols):
        # Calculate the starting position to center blocks horizontally and vertically
        start_x = (window_size[0] - (num_cols * (self.block_width + 5) - 5)) // 2
        start_y = (window_size[1] - (num_rows * (self.block_height + 5) - 5)) // 2

        for row in range(num_rows):
            for col in range(num_cols):
                block_x = start_x + col * (self.block_width + 5)
                block_y = start_y + row * (self.block_height + 5) - 50
                block_color = (255 - row * 40, 0, row * 40)  # Vary color based on row
                block = self.Block(
                    block_x, block_y, self.block_width, self.block_height, block_color
                )
                self.blocks.append(block)

    def draw_blocks(self, screen):
        for block in self.blocks:
            block.draw_me(screen)
