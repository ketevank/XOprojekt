from flask import Flask, render_template, request
from game.Game import *

app = Flask(__name__)

from game.test.fixtures import *

game = Game()  # todo later on keep record of all currrent games, probably in a dict

# todo later on add a http method that will create a new game

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    global game
    playerId = int(request.args.get('playerid'))
    game = Game()
    return render_template('game.jinja2', wynik='', playerId=playerId)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    playerId = int(request.args.get('playerid'))
    return render_template('game.jinja2', wynik = '', playerId = playerId)

@app.route('/cmd', methods=['GET', 'POST'])
def cmd():
    req = request.get_json()
    cmd = req.get('cmd')
    data = req.get('data')
    playerId = int(req.get('playerId'))
    player = game.players[playerId]  # todo get player from request
    if cmd == 'mark' and playerId != game.last_move_player_id:
        x = data['x']
        y = data['y']
        player.mark_field(x, y)
        game.last_move_player_id = playerId

    return game.make_response()

if __name__ == '__main__':
    app.run()
