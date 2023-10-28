import pygame
import sys
from code.ball import Ball
from code.paddle import Paddle
from code.blocks import BlockManager

class Gamer():

    def __init__(self, window_size) -> None:
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.playing = True
        pygame.display.set_caption("Arkanoid Game")
        self.window_size = window_size

        self.paddle = Paddle(window_size)
        self.BlockManager = BlockManager()

    def init_first_level(self):

        self.BlockManager.add_blocks(window_size=self.window_size, num_rows=3, num_cols=6)
        self.ball = Ball(self.window_size)


    def check_collisions(self):

        # Wall Collision
        if self.ball.x <= 0 or self.ball.x >= self.window_size[0]:
            self.ball.speed_x *= -1
        if self.ball.y >= self.window_size[1]:
            return "game over"
        if self.ball.y < 0:
            self.ball.speed_y *= -1

        # Paddle Collision
        if (
            self.paddle.x <= self.ball.x <= self.paddle.x + self.paddle.width
            and self.paddle.y <= self.ball.y + self.ball.size <= self.paddle.y + self.paddle.height
        ):
            relative_intersect_x = (self.paddle.x + self.paddle.width / 2) - self.ball.x
            normalized_intersect_x = relative_intersect_x / (self.paddle.width / -2)

            if normalized_intersect_x < -0.5:
                self.ball.speed_x = self.ball.starting_speed_x * -2
                self.ball.speed_y = self.ball.starting_speed_y / -2
            elif normalized_intersect_x < 0:
                self.ball.speed_x = self.ball.starting_speed_x / -2
                self.ball.speed_y = self.ball.starting_speed_y * -2
            elif normalized_intersect_x < 0.5:
                self.ball.speed_x = self.ball.starting_speed_x / 2
                self.ball.speed_y = self.ball.starting_speed_y * -2
            else:
                self.ball.speed_x = self.ball.starting_speed_x * 2
                self.ball.speed_y = self.ball.starting_speed_y / -2
        
        # Block Collision
        for block in self.BlockManager.blocks.copy():
            if (
            block.x - self.ball.size <= self.ball.x <= block.x + block.width + self.ball.size
            and block.y - self.ball.size <= self.ball.y <= block.y + block.height + self.ball.size
        ):
                block.hits -= 1
                if block.hits == 0:
                    self.BlockManager.blocks.remove(block)
                self.ball.speed_x *= -1
                self.ball.speed_y *= -1
                break


    def game(self):
        while self.playing:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Handle arrow key events for moving the paddle
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.paddle.x > 0:
                self.paddle.go_left()
            if keys[pygame.K_RIGHT] and self.paddle.x < self.window_size[0] - self.paddle.width:
                self.paddle.go_right()

            # Draw Screen
            self.screen.fill((0, 0, 0))
            self.paddle.draw_me(self.screen)
            self.ball.draw_me(self.screen)
            self.BlockManager.draw_blocks(self.screen)

            # Check for collisions
            self.ball.move()
            result = self.check_collisions()
            if result == "game over":
                self.playing = False

            # Update the display
            pygame.display.flip()

            # Limit frames per second
            pygame.time.Clock().tick(60)