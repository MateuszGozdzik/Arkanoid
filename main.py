from code.game import Gamer
# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)


gamer = Gamer(WINDOW_SIZE)

gamer.init_first_level()
gamer.game()