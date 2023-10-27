import pygame
import sys
from objects import Paddle, Ball, BlockManager

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Arkanoid Game")

ball = Ball(WIDTH, HEIGHT)
paddle = Paddle(WIDTH, HEIGHT)
BlockManager = BlockManager()

BlockManager.add_blocks(WINDOW_SIZE, 3, 6)


# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle arrow key events for moving the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.go_left()
    if keys[pygame.K_RIGHT] and paddle.x < WIDTH - paddle.width:
        paddle.go_right()

    # Draw Screen
    screen.fill((0, 0, 0))
    paddle.draw_me(screen)
    ball.draw_me(screen)
    BlockManager.draw_blocks(screen)

    # Check for collisions
    ball.move()
    ball.check_wall_collisions(WINDOW_SIZE)
    ball.check_paddle_collision(paddle)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)
