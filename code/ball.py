import pygame


class Ball:
    def __init__(self, window_size) -> None:
        self.size = 20
        self.x, self.y = window_size[0] // 2, window_size[1] // 1.5
        self.starting_speed_x, self.starting_speed_y = 5, 5
        self.speed_x, self.speed_y = self.starting_speed_x, self.starting_speed_y

    def draw_me(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

