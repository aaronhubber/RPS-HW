from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/video')
def video():
    return render_template ("video.html", title="Video")

@app.route('/origin')
def origin_story():
    return render_template ("origin.html", title="Origin Story")

@app.route('/game', methods=['POST'])
def game_result():
    player1_name = request.form["name1"]
    player1_weapon = request.form["weapon1"]

    player2_name = request.form["name2"]
    player2_weapon = request.form["weapon2"]

    player1 = Player(player1_name, player1_weapon)
    player2 = Player(player2_name, player2_weapon)


    game = Game(player1, player2)
    game_result = game.play_game()
    
    return render_template("index.html", title="result", result=game_result)

# @app.route('/play')
# def man_vs_machine(play):
#     player1_name = request.form["name1"]
#     player1_weapon = request.form["weapon1"]

#     player1 = Player(player1_name, player1_weapon)

#     game = Game(player1)
#     game_result = game.play_computer()

#     return render_template("index.html", title="result", result=game_result)

