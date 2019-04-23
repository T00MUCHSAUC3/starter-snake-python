from flask import Flask, request, jsonify
import os, random, math, controller
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
    data = request.get_json()
    
    print(data) 

@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

@app.route("/end", methods=["POST"])
def end(): 
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
