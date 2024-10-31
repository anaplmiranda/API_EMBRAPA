from flask import jsonify
from app import app
from app.auth_jwt import token_creator, token_verify


@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/hello', methods=['GET'])
@token_verify
def hello(token):
    return jsonify({
        "message": "Hello, World!",
        'token': token
    }),200