from flask import jsonify
from app import app, auth

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/hello', methods=['GET'])
@auth.login_required
def hello():
    return jsonify({"message": "Hello, World!"})