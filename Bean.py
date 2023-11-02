import random

from constants import WIDTH, HEIGHT

class Bean:
    def __init__(self):
        self.position = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
