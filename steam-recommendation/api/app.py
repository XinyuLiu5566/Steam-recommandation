import time
import json
import requests
from flask import Flask
from process import *

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/get_game",methods=["POST", "GET"])
def get_game():
    data = request.get_json(force=True)
    name = data["name"]
    result = []

    # data是前端返回的JSON数据，包含名称和时间
    # 加入Jupyter note的后端代码计算返回数据
    # 包括读取数据集的所有游戏
    # 返回推荐游戏名称

    # api在前端的react调用方式通过flask + react
    # flask端口是 http://127.0.0.1:5000/get_game or http://localhost:5000/get_game
    # 后端启动方式yarn start-api
    # 前端启用可以改成 yarn start
    
    if result:
        return {'rec': result}
    else:
        return {'rec': 0}


# testing
user_profile = [["DARK SOULS III", 286], ['Grand Theft Auto V', 45], ['Portal 2', 8], ['RESIDENT EVIL 7 biohazard  BIOHAZARD 7 resident evil', 88], ['Sekiro Shadows Die Twice', 1.4]]

# these two lines of codes only need to run for once
content_data = set_up()
tfidf, list_app_name = tf_idf(content_data)

# get recommendation list from an input user profile
def get_recommendation(user_profile, content_data, tfidf, list_app_name):
    names = []
    for i in range(len(user_profile)):
        names.append(user_profile[i][0])
        if user_profile[i][1] <= 2:
            user_profile[i][1] = 0.1
        elif user_profile[i][1] > 2 and user_profile[i][1] <= 10:
            user_profile[i][1] = 0.5
        elif user_profile[i][1] > 10 and user_profile[i][1] <= 50:
            user_profile[i][1] = 0.8
        elif user_profile[i][1] > 50 and user_profile[i][1] <= 100: 
            user_profile[i][1] = 1
        else:
            user_profile[i][1] = 1.2

    recommendations = {}
    for game in user_profile:
        name = game[0]
        id = content_data.index[content_data['Game_name'] == name][0]
        similarities = linear_kernel(tfidf[id],tfidf).flatten()
        related_docs_indices = (-similarities).argsort()[1:11]
        lam = 0
        for i in related_docs_indices:
            new_game = list_app_name[i]
            if new_game not in names:
                if new_game not in recommendations:
                    recommendations.update({new_game: game[1]-lam})
                else:
                    value = recommendations.get(new_game)
                    recommendations.update({new_game: value+game[1]-lam})
            lam += 0.01

    recommendations = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))

    output = []
    count = 0
    for key in recommendations:
        output.append(key)
        count += 1
        if count >= 10:
            break

    return output

output = get_recommendation(user_profile, content_data, tfidf, list_app_name)
print(output)