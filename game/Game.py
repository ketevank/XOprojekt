import math
import random

from game.Player import *
import json

class Game:

    def __init__(self):
        self.last_move_player_id = round(random.random())
        self.players = {}
        self.turn = ''

    def make_response(self):
        dumps = json.dumps(self, default=lambda x: x.__dict__)
        return dumps
