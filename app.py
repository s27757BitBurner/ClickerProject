from flask import Flask, render_template, jsonify

app = Flask(__name__)
score = 0
# implementation for web based approach
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    global score
    score += 1
    return jsonify(score=score)

if __name__ == '__main__':
    app.run(debug=True)
