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
