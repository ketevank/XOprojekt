from game.Sign import Sign

class Field:
    x = 0
    y = 0

    def __init__(self, x:int, y:int):  #w argumentach określone paremetry x i y (które to pole na planszy)
        self.x = x
        self.y = y

    def get_column_line(self):
        return self.x

    def get_row_line(self):
        return self.y

    def get_slash_line(self):
        return self.x + self.y

    def get_backslash_line(self):
        return self.x - self.y

    def __eq__(self, other):
        if not isinstance(other, Field):
            raise AttributeError('Pole porównywane z nie polem')
        if self.x == other.x and self.y ==other.y:
            return True

        return False