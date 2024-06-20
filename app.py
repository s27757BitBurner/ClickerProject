from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
# MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.clicker_game
scores_collection = db.scores

#variables
score = 0
username = ''
# implementation for web based approach
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/start', methods=['POST'])
def start_game():
    global username, score
    username = request.json.get('username')
    score = 0
    return jsonify(message='Game started', username=username, score=score)

@app.route('/click', methods=['POST'])
def click():
    global score
    score += 1
    return jsonify(score=score)
@app.route('/save', methods=['POST'])
def save_score():
    global username, score
    if username:
        scores_collection.update_one(
            {'username': username},
            {'$set': {'high_score': score}},
            upsert=True
        )
        return jsonify(message='Score saved', username=username, high_score=score)
    return jsonify(message='No username set'), 400

if __name__ == '__main__':
    app.run(debug=True)
