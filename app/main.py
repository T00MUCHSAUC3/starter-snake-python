from flask import Flask, request, jsonify
import os, random, math, MasterTower
from datetime import datetime
from timeit import default_timer as timer

app = Flask(__name__.split('.')[0]) 

@app.route("/start", methods=["POST"]) 
def start():
    global width
    global height
    global game_id

    #NOTE NOT SURE WHAT JSONIFY IS DOING JUST YET FIGURE THIS OUT
    return jsonify( color = "000000", secondary_color = "#000000", name = "SLIMEYSNAKE", taunt = "SLIME GANG DADDY", head_type="evil", tail_type="bolt", head_url="https://pbs.twimg.com/profile_images/919244128843653120/6NE6SBBL_400x400.jpg")

@app.route("/move", methods=["POST"])
def move():
    debug = True
    data = request.get_json()
    print(data)
    
    game = data.get("game")
    game_id = data.get("id")
    turn = data.get("food")

    #NOTE Get everything that our snake will need to know, i.e. everything to set up our grid.
    board = data.get("board")
    height = board.get("height")
    width = board.get("width")
    food = data.get("board").get("food")
    snakes = data.get("board").get("snakes")

    #NOTE Get all the information about our snake
    thisSnake = data.get("you")
    thisHealth = thisSnake.get("health")
    thisBody = thisSnake.get("body")

    #NOTE Batch above groups of information into tuples to pass into master
    environment = (board, height, width, food, snakes)
    ourSnake = (thisSnake, thisHealth, thisBody)

    #NOTE MasterTower is where the magic happens
    result = MasterTower.initGrid(environment, ourSnake)

    if debug:
        start = timer()
        print('')
        print("Health:{}".format(thisHealth))
        print('')
        print("Game height:{} , Game width: {}".format(height, width))
        print('')
        print('turn = {}'.format(data.get("turn")))
        print('')

    print(result)

@app.route("/end", methods=["POST"])
def end(): 
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
