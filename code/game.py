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
        pygame.display.set_caption("Arkanoid Game")
        self.window_size = window_size

        self.paddle = Paddle(window_size)
        self.BlockManager = BlockManager()

    def init_first_level(self):

        self.BlockManager.add_blocks(window_size=self.window_size, num_rows=3, num_cols=6)
        self.ball = Ball(self.window_size)

    def game(self):
        while True:
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
            self.ball.check_wall_collisions(self.window_size)
            self.ball.check_paddle_collision(self.paddle)

            # Update the display
            pygame.display.flip()

            # Limit frames per second
            pygame.time.Clock().tick(60)