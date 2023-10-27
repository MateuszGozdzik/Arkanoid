import pygame


class Paddle:
    def __init__(self, width, height) -> None:
        self.width, self.height = 300, 10
        self.x = (width - self.width) // 2
        self.y = height - 20
        self.speed = 8

    def go_left(self):
        self.x -= self.speed

    def go_right(self):
        self.x += self.speed

    def draw_me(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))


class Ball:
    def __init__(self, width, height) -> None:
        self.size = 20
        self.x, self.y = width // 2, height // 2
        self.speed_x, self.speed_y = 5, 5

    def draw_me(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_wall_collisions(self, window_size):
        if self.x <= 0 or self.x >= window_size[0]:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= window_size[1]:
            self.speed_y *= -1


class BlockManager():

    class Block():
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            
        def draw_me(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    


    def __init__(self) -> None:
            
            self.block_width, self.block_height = 80, 30
            self.blocks = []

    def add_blocks(self, window_size, num_rows, num_cols):
        

        # middle_x, middle_y = window_size[0] / 2, window_size[1] / 2
        # if num_rows % 2 == 0:
        #     middle_x -= self.block_height / 2 

        for row in range(num_rows):
            for col in range(num_cols):
                block_x = col * (self.block_width + 5) + 50
                block_y = row * (self.block_height + 5) + 50
                block_color = (255 - row * 40, 0, row * 40)  # Vary color based on row
                block = self.Block(block_x, block_y, self.block_width, self.block_height, block_color)
                self.blocks.append(block)
    
    def draw_blocks(self, screen):
        for block in self.blocks:
            block.draw_me(screen)