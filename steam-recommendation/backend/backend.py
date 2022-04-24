import flask
import json
import requests
import re

@app.route("/get_game_url",methods=["POST", "GET"])
def get_game():
    data = request.get_json(force=True)
    name = data["name"]
    result = [i for i in result]
    if result:
        return {'rec': result}
    else:
        return {'rec': 0}