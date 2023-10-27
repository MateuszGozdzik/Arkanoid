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
