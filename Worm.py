from constants import LEFT, RIGHT, UP, DOWN

class Worm:
    def __init__(self):
        self.body = [(1, 5), (1, 4), (1, 3), (1, 2), (1, 1)]
        self.direction = DOWN

    def head(self):
        return self.body[0]

    def move(self):
        head_x, head_y = self.head()
        new_dir_x, new_dir_y = self.direction
        new_pos = ((head_x + new_dir_x), (head_y + new_dir_y))

        self.body = [new_pos] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def up(self):
        if self.direction != DOWN:
            self.direction = UP

    def down(self):
        if self.direction != UP:
            self.direction = DOWN
