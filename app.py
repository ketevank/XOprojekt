import uuid

from flask import Flask, render_template, request

app = Flask(__name__)

from game.test.fixtures import *

games = dict()

@app.route('/newsession', methods=['GET', 'POST'])
def newSession():
    sessionId = str(uuid.uuid1())
    games[sessionId] = Game()
    return sessionId

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.jinja2')



@app.route('/list', methods=['GET', 'POST'])
def list():
    return render_template('listOfGames.jinja2')


@app.route('/restart', methods=['GET', 'POST'])
def restart():
    sessionId = request.args.get('sessionid')
    prevGame = games[sessionId]
    for player in prevGame.players.values():
        player.clear()

    return render_template('game.jinja2')


@app.route('/', methods=['GET', 'POST'])
def gameBoard():
    return render_template('listOfGames.jinja2')


# @app.route('/', methods=['GET', 'POST'])
# def gameBoard():
#     return render_template('game.jinja2', wynik='')


@app.route('/cmd', methods=['POST'])
def cmd():
    req = request.get_json()
    cmd = req.get('cmd')
    data = req.get('data')
    sessionId = req.get('sessionid')
    game = games[sessionId]

    playerId = req.get('playerid')
    if cmd == 'mark' and playerId != game.last_move_player_id and game.players.keys().__len__() == 2:
        player = game.players[playerId]
        x = data['x']
        y = data['y']
        player.mark_field(x, y)
        game.last_move_player_id = playerId

    response = game.make_response()
    return response


@app.route('/gameslist', methods=['GET', 'POST'])
def createListOfGames():
    keys = [str(key) for key in games.keys() if games[key].players.__len__() < 2]
    dumps = json.dumps(keys)
    return dumps


@app.route('/joingame', methods=['GET', 'POST'])
def joinPlayer():
    sessionId = request.args.get('sessionid')
    game = games[sessionId]
    playerId = str(uuid.uuid1())
    if game.players.keys().__len__() == 0:
        player = Player(Sign.X)
        game.players[playerId] = player
        return json.dumps({'playerid': playerId})
    elif game.players.keys().__len__() == 1:
        player = Player(Sign.O)
        game.players[playerId] = player
        return json.dumps({'playerid': playerId})
    else:
        return "error"

if __name__ == '__main__':
    app.run()
