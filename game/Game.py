import math
import random

from game.Player import *
import json

class Game:
    last_move_player_id = round(random.random())
    players = []  # tablica graczy
    turn = ''

    def __init__(self):
        self.players = [Player(Sign('X')), Player(Sign('O'))]  # dwóch graczy w tablicy
        # self.turn = Sign('O').value  # zaczynają kółka

    def make_response(self):
        return json.dumps(self, default=lambda x: x.__dict__)
