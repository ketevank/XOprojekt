from game.Game import *

def _XX():
    game = Game()
    game.players[0].marked_fields = [Field(1,2), Field(1,3)]
    return game

def OXX():
    arrayX = [Field(1,2), Field(1,3)]
    arrayO = [Field(1,1)]
    return make_game_fixure(arrayX, arrayO)

def OXX__PP():
    arrayX = [Field(1,2), Field(1,3), Field(2,2), Field(2,3)]
    arrayO = [Field(1,1)]
    return make_game_fixure(arrayX, arrayO)

def XPP_XPO_XPP():
    arrayX = [Field(1,1), Field(2,1), Field(3,1)]
    arrayO = [Field(2,3)]
    return make_game_fixure(arrayX, arrayO)

def make_game_fixure(arrayX, arrayO, turn = 'O'):
    game = Game()
    game.players[0].marked_fields = arrayX
    game.players[1].marked_fields = arrayO
    return game
