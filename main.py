from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

#choices 
choices = ['rock', 'paper', 'scissors']
rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = 'tie'
    elif rules[user_choice] == computer_choice:
        result = 'win'
    else:
        result = 'lose'

    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
