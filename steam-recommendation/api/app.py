import time
import json
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/get_game",methods=["POST", "GET"])
def get_game():
    data = request.get_json(force=True)
    name = data["name"]
    result = []

    // data是前端返回的JSON数据，包含名称和时间
    // 加入Jupyter note的后端代码计算返回数据
    // 包括读取数据集的所有游戏
    // 返回推荐游戏名称

    // api在前端的react调用方式通过flask + react
    // flask端口是 http://127.0.0.1:5000/get_game or http://localhost:5000/get_game
    // 后端启动方式yarn start-api
    // 前端启用可以改成 yarn start
    
    if result:
        return {'rec': result}
    else:
        return {'rec': 0}
