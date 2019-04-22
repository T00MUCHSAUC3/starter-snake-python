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
    return jsonify( color = "#E0FFFF", secondary_color = "#000000", name = "SLIMEYSNAKE", taunt = "SLIME GANG DADDY", head_type="shades", tail_type="freckled", head_url="https://pbs.twimg.com/profile_images/919244128843653120/6NE6SBBL_400x400.jpg")

@app.route("/move", methods=["POST"])
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
