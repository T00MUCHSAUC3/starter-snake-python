from flask import Flask, request, jsonify
import os, random, math
from datetime import datetime
from timeit import default_timer as timer

app = Flask(__name__) 

@app.route("/start", methods=["POST"]) 
def start():
    global width
    global height
    global game_id

    #NOTE NOT SURE WHAT JSONIFY IS DOING JUST YET FIGURE THIS OUT
    return jsonify( color = "#E0FFFF", secondary_color = "#000000", name = "SLIMEYSNAKE", taunt = "SLIME GANG DADDY", head_type="evil", tail_type="bolt", head_url="https://pbs.twimg.com/profile_images/919244128843653120/6NE6SBBL_400x400.jpg")

@app.route("/move", methods=["POST"])
def move():
    debug = True
    data = request.get_json()
    
    game = data.get("game")
    game_id = data.get("id")
    turn = data.get("food")
    board = data.get("board")
    height = data.get("board").get("height")
    width = data.get("board").get("width")

    myHealth = you.get("health")

    if debug:
        start = timer()
        print('')
        print("Health:{}".format(myHealth))
        print('')
        print("Game height:{} , Game width: {}".format(height, width))
        print('')
        print('turn = {}'.format(data.get("turn")))

@app.route("/end", methods=["POST"])
def end(): 
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
