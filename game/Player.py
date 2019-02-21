from game.Field import *


class Player:
    marked_fields = []
    sign = ''
    hasWinningPosition = False
    scoreDraw = False

    # todo add property for a player that has a winning position
    def __init__(self, sign: Sign):
        self.sign = sign.value
        self.marked_fields = []  # tablica zaznaczonych pól

    def mark_field(self, x: int, y: int):  # metoda zaznaczania pola
        field = Field(x, y)
        self.marked_fields.append(field)  # dodawanie pola do tablicy marked_fields
        result = self.count_x_in_line()
        if result == 3:
            self.hasWinningPosition = True
        elif len(self.marked_fields) == 5:
            self.scoreDraw = True

    #     todo check if this move gave a player winning poisition and store this status

    def get_stats(self):
        stats = {'1r': 0, '2r': 0, '3r': 0, '1c': 0}
        pass

    def count_x_in_line(self):
        maxResult = 0
        for n in range(1,4):
            results_horizontal = [field for field in self.marked_fields if field.x == n].__len__()
            maxResult = max(results_horizontal, maxResult)
        for n in range(1,4):
            results_vertical = [field for field in self.marked_fields if field.y == n].__len__()
            maxResult = max(results_vertical, maxResult)

        results_diagonal = [field for field in self.marked_fields for n in range(1,4) if field.y == n and field.x == n].__len__()
        maxResult = max(results_diagonal, maxResult)
        reversed_results_diagonal = [field for field in self.marked_fields for n in range(1,4) if field.y == n and field.x == 4 - n].__len__()
        maxResult = max(reversed_results_diagonal, maxResult)
        return maxResult
