from flask import Flask, send_from_directory, request, jsonify
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    secret_number = int(request.form['secret_number'])
    response = ''

    if user_guess < secret_number:
        response = 'Lebih Tinggi Lagi!'
    elif user_guess > secret_number:
        response = 'Lebih Rendah Lagi!'
    else:
        response = 'Habat, angka tebakan kamu benar!'

    return jsonify(result=response)

@app.route('/secret')
def secret():
    secret_number = random.randint(1, 100)
    return jsonify(secret_number=secret_number)

if __name__ == '__main__':
    app.run(debug=True)
