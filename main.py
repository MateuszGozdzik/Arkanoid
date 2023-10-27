import pygame
import sys
from objects import Paddle, Ball

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

    # Clear the screen
    screen.fill(WHITE)

    paddle.draw_me(screen)
    ball.draw_me(screen)

    ball.move()
    ball.check_wall_collisions(WINDOW_SIZE)

    # Ball collision with paddle
    if paddle.x <= ball.x <= paddle.x + paddle.width and paddle.y <= ball.y + ball.size <= paddle.y + paddle.height:
        ball.speed_y *= -1

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(60)