import pygame


class Ball:
    def __init__(self, width, height) -> None:
        self.size = 20
        self.x, self.y = width // 2, height // 2
        self.starting_speed_x, self.starting_speed_y = 5, 5
        self.speed_x, self.speed_y = self.starting_speed_x, self.starting_speed_y

    def draw_me(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_wall_collisions(self, window_size):
        if self.x <= 0 or self.x >= window_size[0]:
            self.speed_x *= -1
        if self.y >= window_size[1]:
            pass
            # *
            # TODO GAME OVER
            # ?
        if self.y < 0:
            self.speed_y *= -1

    def check_paddle_collision(self, paddle):
        if (
            paddle.x <= self.x <= paddle.x + paddle.width
            and paddle.y <= self.y + self.size <= paddle.y + paddle.height
        ):
            relative_intersect_x = (paddle.x + paddle.width / 2) - self.x
            normalized_intersect_x = relative_intersect_x / (paddle.width / -2)
            print(normalized_intersect_x)

            if normalized_intersect_x < -0.5:
                self.speed_x = self.starting_speed_x * -2
                self.speed_y = self.starting_speed_y / -2
            elif normalized_intersect_x < 0:
                self.speed_x = self.starting_speed_x / -2
                self.speed_y = self.starting_speed_y * -2
            elif normalized_intersect_x < 0.5:
                self.speed_x = self.starting_speed_x / 2
                self.speed_y = self.starting_speed_y * -2
            else:
                self.speed_x = self.starting_speed_x * 2
                self.speed_y = self.starting_speed_y / -2
